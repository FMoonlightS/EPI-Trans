
import tensorflow as tf
from tensorflow.keras.layers import *
from tensorflow.keras.models import *
import numpy as np
from transfomer import Transformer_Merged

merged_n_heads=9
merged_feed_forward_size=256
merged_encoder_stack=1

en_pool_size=15
pr_pool_size=10
en_strides=en_pool_size
pr_strides=pr_pool_size

en_kernal_size = 80
pr_kernal_size = 61

num_filters = 72
model_dim = num_filters

def get_model(max_len_en, max_len_pr, nwords, emb_dim):

    enhancers = Input(shape=(max_len_en,))
    promoters = Input(shape=(max_len_pr,))

    embedding_matrix = np.load('embedding_matrix.npy')

    emb_en = Embedding(nwords, emb_dim,
                     weights=[embedding_matrix],trainable=True)(enhancers) # dna2vec embedding layer for enhancer
    emb_pr = Embedding(nwords, emb_dim,
                     weights=[embedding_matrix],trainable=True)(promoters) # dna2vec embedding layer for promoter

    enhancer_conv_layer = Conv1D(filters=num_filters,
                                 kernel_size=en_kernal_size,
                                 padding="valid",
                                 activation='relu')(emb_en)

    enhancer_max_pool_layer = MaxPooling1D(pool_size=en_pool_size, strides=en_strides)(enhancer_conv_layer)

    promoter_conv_layer = Conv1D(filters=num_filters,
                                 kernel_size=pr_kernal_size,
                                 padding="valid",
                                 activation='relu')(emb_pr)

    promoter_max_pool_layer = MaxPooling1D(pool_size=pr_pool_size, strides=pr_strides)(promoter_conv_layer)

    # merge
    merge=Concatenate(axis=1)([enhancer_max_pool_layer, promoter_max_pool_layer])

    bn=BatchNormalization()(merge)

    dt=Dropout(0.5)(bn)

    transformer1 = Transformer_Merged(encoder_stack=merged_encoder_stack,
                                feed_forward_size=merged_feed_forward_size,
                                n_heads=merged_n_heads,
                                model_dim=model_dim)

    trf = transformer1(dt)

    Gmaxpool = GlobalMaxPooling1D()(trf)

    merge2 = Dense(50)(Gmaxpool)

    bn2=BatchNormalization()(merge2)

    acti = Activation('relu')(bn2)

    preds = Dense(1, activation='sigmoid')(acti)

    model = Model([enhancers, promoters], preds)

    # opt = tf.keras.optimizers.Nadam(learning_rate=0.01)

    opt = tf.keras.optimizers.Nadam()

    model.compile(loss='binary_crossentropy', optimizer=opt)

    return model