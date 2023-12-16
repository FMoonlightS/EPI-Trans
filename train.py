# --------------------------------------------------------------------
# To compare with pioneers, we quoted some of the train procedure from EPIVAN
# --------------------------------------------------------------------


from model import get_model
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
import os

os.environ["CUDA_VISIBLE_DEVICES"]="2"

index = 0
# gen_index = 6
batch_size=64
epochs=20
# gen_epochs=25
names = ['GM12878', 'HeLa-S3', 'HUVEC', 'IMR90', 'K562', 'NHEK', 'all']
name = names[index]
Data_dir = './data/%s/'%name
max_len_en = 3000
max_len_pr = 2000
nwords = 4097
emb_dim = 100

# checkpoint_path = "models/General/cp-{epoch:04d}.ckpt"  # this the location of the general model which used a pre-trained model for training the best models
# checkpoint_dir = os.path.dirname(checkpoint_path)

model = get_model(max_len_en, max_len_pr, nwords, emb_dim)

# latest = tf.train.latest_checkpoint(checkpoint_dir)
# model.load_weights(latest)

train = np.load(Data_dir+'%s_train.npz'% name) # load the training data

X_en_tra, X_pr_tra, y_tra = train['X_en_tra'], train['X_pr_tra'], train['y_tra']

X_en_tra, X_en_val, X_pr_tra, X_pr_val, y_tra, y_val = train_test_split(
    X_en_tra, X_pr_tra, y_tra, test_size=0.05,stratify=y_tra, random_state=250)

# opt = tf.keras.optimizers.Nadam(learning_rate=0.01)
opt = tf.keras.optimizers.Nadam()
model.compile(loss='binary_crossentropy', optimizer=opt,
              metrics=['acc'])
model.summary()

# Include the epoch in the file name (uses `str.format`)
# checkpoint_path = "models/General/cp-{epoch:04d}.ckpt"
# checkpoint_path = "models/Best/GM12878/cp-{epoch:04d}.ckpt"

checkpoint_path = "models/Specific/GM12878/cp-{epoch:04d}.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

# Create a callback that saves the model's weights every 1 epochs
cp_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_path,
    verbose=1,
    save_weights_only=True,
    save_freq=5*batch_size)

# Save the weights using the `checkpoint_path` format
model.save_weights(checkpoint_path.format(epoch=0))

history = model.fit([X_en_tra, X_pr_tra], y_tra,
                    validation_data=([X_en_val, X_pr_val], y_val),
                    epochs=epochs, batch_size=batch_size,
                    callbacks=[cp_callback],
                    verbose=0
                    )
