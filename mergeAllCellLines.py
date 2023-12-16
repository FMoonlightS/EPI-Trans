
import itertools as it


names = ['GM12878', 'HeLa-S3', 'HUVEC', 'IMR90', 'K562', 'NHEK']

name = names[0]
train_dir='./data/%s/train/'%name
GM12878_enhancers_tra=open(train_dir+'%s_enhancer.fasta'%name,'r').read().splitlines()[1::2]
GM12878_promoters_tra=open(train_dir+'%s_promoter.fasta'%name,'r').read().splitlines()[1::2]
GM12878_y_tra        =open(train_dir+'%s_label.txt'%name,'r').read().splitlines()
print("GM12878_y : ", str(len(GM12878_y_tra)))
print("GM12878_en : ", str(len(GM12878_enhancers_tra)))
print("GM12878_pr : ", str(len(GM12878_promoters_tra)))

name = names[1]
train_dir='./data/%s/train/'%name
HeLa_S3_enhancers_tra=open(train_dir+'%s_enhancer.fasta'%name,'r').read().splitlines()[1::2]
HeLa_S3_promoters_tra=open(train_dir+'%s_promoter.fasta'%name,'r').read().splitlines()[1::2]
HeLa_S3_y_tra        =open(train_dir+'%s_label.txt'%name,'r').read().splitlines()
print("HeLa-S3_y : ", str(len(HeLa_S3_y_tra)))
print("HeLa-S3_en : ", str(len(HeLa_S3_enhancers_tra)))
print("HeLa-S3_pr : ", str(len(HeLa_S3_promoters_tra)))

name = names[2]
train_dir='./data/%s/train/'%name
HUVEC_enhancers_tra=open(train_dir+'%s_enhancer.fasta'%name,'r').read().splitlines()[1::2]
HUVEC_promoters_tra=open(train_dir+'%s_promoter.fasta'%name,'r').read().splitlines()[1::2]
HUVEC_y_tra        =open(train_dir+'%s_label.txt'%name,'r').read().splitlines()
print("HUVEC_y : ", str(len(HUVEC_y_tra)))
print("HUVEC_en : ", str(len(HUVEC_enhancers_tra)))
print("HUVEC_pr : ", str(len(HUVEC_promoters_tra)))

name = names[3]
train_dir='./data/%s/train/'%name
IMR90_enhancers_tra=open(train_dir+'%s_enhancer.fasta'%name,'r').read().splitlines()[1::2]
IMR90_promoters_tra=open(train_dir+'%s_promoter.fasta'%name,'r').read().splitlines()[1::2]
IMR90_y_tra        =open(train_dir+'%s_label.txt'%name,'r').read().splitlines()
print("IMR90_y : ", str(len(IMR90_y_tra)))
print("IMR90_en : ", str(len(IMR90_enhancers_tra)))
print("IMR90_pr : ", str(len(IMR90_promoters_tra)))

name = names[4]
train_dir='./data/%s/train/'%name
K562_enhancers_tra=open(train_dir+'%s_enhancer.fasta'%name,'r').read().splitlines()[1::2]
K562_promoters_tra=open(train_dir+'%s_promoter.fasta'%name,'r').read().splitlines()[1::2]
K562_y_tra        =open(train_dir+'%s_label.txt'%name,'r').read().splitlines()
print("K562_y : ", str(len(K562_y_tra)))
print("K562_en : ", str(len(K562_enhancers_tra)))
print("K562_pr : ", str(len(K562_promoters_tra)))

name = names[5]
train_dir='./data/%s/train/'%name
NHEK_enhancers_tra=open(train_dir+'%s_enhancer.fasta'%name,'r').read().splitlines()[1::2]
NHEK_promoters_tra=open(train_dir+'%s_promoter.fasta'%name,'r').read().splitlines()[1::2]
NHEK_y_tra        =open(train_dir+'%s_label.txt'%name,'r').read().splitlines()
print("NHEK_y : ", str(len(NHEK_y_tra)))
print("NHEK_en : ", str(len(NHEK_enhancers_tra)))
print("NHEK_pr : ", str(len(NHEK_promoters_tra)))

all_enhancers_tra = []
all_promoters_tra = []
all_y_tra = []
for (GM12878_en, GM12878_pr, GM12878_y,
    HeLa_S3_en , HeLa_S3_pr, HeLa_S3_y,
    HUVEC_en, HUVEC_pr, HUVEC_y,
    IMR90_en, IMR90_pr, IMR90_y,
    K562_en, K562_pr, K562_y,
    NHEK_en, NHEK_pr, NHEK_y) in it.zip_longest(GM12878_enhancers_tra, GM12878_promoters_tra, GM12878_y_tra,
                                                HeLa_S3_enhancers_tra, HeLa_S3_promoters_tra, HeLa_S3_y_tra,
                                                HUVEC_enhancers_tra, HUVEC_promoters_tra, HUVEC_y_tra,
                                                IMR90_enhancers_tra, IMR90_promoters_tra, IMR90_y_tra,
                                                K562_enhancers_tra, K562_promoters_tra, K562_y_tra,
                                                NHEK_enhancers_tra, NHEK_promoters_tra, NHEK_y_tra):
    if GM12878_en != None: all_enhancers_tra.append(GM12878_en)
    if HeLa_S3_en != None: all_enhancers_tra.append(HeLa_S3_en)
    if HUVEC_en   != None: all_enhancers_tra.append(HUVEC_en)
    if IMR90_en   != None: all_enhancers_tra.append(IMR90_en)
    if K562_en    != None: all_enhancers_tra.append(K562_en)
    if NHEK_en    != None: all_enhancers_tra.append(NHEK_en)

    if GM12878_pr != None: all_promoters_tra.append(GM12878_pr)
    if HeLa_S3_pr != None: all_promoters_tra.append(HeLa_S3_pr)
    if HUVEC_pr   != None: all_promoters_tra.append(HUVEC_pr)
    if IMR90_pr   != None: all_promoters_tra.append(IMR90_pr)
    if K562_pr    != None: all_promoters_tra.append(K562_pr)
    if NHEK_pr    != None: all_promoters_tra.append(NHEK_pr)

    if GM12878_y != None: all_y_tra.append(GM12878_y)
    if HeLa_S3_y != None: all_y_tra.append(HeLa_S3_y)
    if HUVEC_y   != None: all_y_tra.append(HUVEC_y)
    if IMR90_y   != None: all_y_tra.append(IMR90_y)
    if K562_y    != None: all_y_tra.append(K562_y)
    if NHEK_y    != None: all_y_tra.append(NHEK_y)


with open("data/all/all_enhancers_tra.fasta","w") as f:
    for line in all_enhancers_tra:
        f.write(">\n")
        f.write(line)
        f.write("\n")
f.close()

with open("data/all/all_promoters_tra.fasta","w") as f:
    for line in all_promoters_tra:
        f.write(">\n")
        f.write(line)
        f.write("\n")
f.close()

with open("data/all/all_y_tra.txt","w") as f:
    for line in all_y_tra:
        f.write(line)
        f.write("\n")
f.close()

print("all_y : ", str(len(all_y_tra)))
print("all_en : ", str(len(all_enhancers_tra)))
print("all_pr : ", str(len(all_promoters_tra)))
