# --------------------------------------------------------------------
# To compare with pioneers, we quoted some of the test procedure from EPIVAN
# --------------------------------------------------------------------
import os
import tensorflow as tf
from models import get_model


os.environ["CUDA_VISIBLE_DEVICES"]="2"

import numpy as np
from sklearn.metrics import roc_auc_score,average_precision_score


models=['GM12878', 'HeLa-S3', 'HUVEC', 'IMR90', 'K562', 'NHEK','all']
index = 5
batch_size=64

m=models[index]
model=None

max_len_en = 3000
max_len_pr = 2000
nwords = 4097
emb_dim = 100

# checkpoint_path = "models/General/cp-{epoch:04d}.ckpt"
# checkpoint_path = "models/Best/GM12878/cp-{epoch:04d}.ckpt"

checkpoint_path = "models/Specific/GM12878/cp-{epoch:04d}.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

model = get_model(max_len_en, max_len_pr, nwords, emb_dim)

latest = tf.train.latest_checkpoint(checkpoint_dir)
model.load_weights(latest)

names = ['GM12878', 'HeLa-S3', 'HUVEC', 'IMR90', 'K562', 'NHEK']

for name in names:
    Data_dir='./data/%s/' % name
    test=np.load(Data_dir+'%s_test.npz'%name)
    X_en_tes,X_pr_tes,y_tes=test['X_en_tes'],test['X_pr_tes'],test['y_tes']
    print("****************Testing %s cell line specific model on %s cell line****************"%(m,name))
    y_pred = model.predict([X_en_tes,X_pr_tes])
    auc=roc_auc_score(y_tes, y_pred)
    aupr=average_precision_score(y_tes, y_pred)
    print("AUC : ", auc)
    print("AUPR : ", aupr)
