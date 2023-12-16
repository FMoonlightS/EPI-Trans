# EPI-Trans: An Effective Transformer-based Deep Learning Model for Enhancer Promoter Interaction Prediction
Recognition of Enhancer-Promoter Interactions (EPIs) is crucial for human development. EPIs in the genome play a key role in regulating transcription. However, experimental approaches for classifying EPIs are too expensive in terms of effort, time, and resources. Therefore, more and more studies are being done on developing computational techniques, particularly using deep learning and other machine learning techniques, to address such problems. Unfortunately, the majority of current computational methods are based on convolutional neural networks, recurrent neural networks, or a combination of them, which don't take into consideration contextual details and the long-range interactions between the enhancer and promoter sequences. A new transformer-based model called EPI-Trans is presented in this study to overcome the aforementioned limitations. The multi-head attention mechanism in the transformer model automatically learns features that represent the long interrelationships between enhancer and promoter sequences.  Furthermore,  a generic model is created with transferability that can be utilized as a pre-trained model for various cell lines.  Moreover, the parameters of the generic model are fine-tuned using a particular cell line dataset to improve performance. The comparative results on certain cell lines show that EPI-Trans outperforms other cutting-edge techniques. Based on the results obtained from six benchmark cell lines, the average AUROC for the specific, generic, and best models is 94.2%, 95%, and 95.7%, while the average AUPR is 80.5%, 66.1%, and 79.6% respectively.

# File Description 
- Data_Augmentation.R

  A tool for data augmentation was provided by Mao et al. (2017). The details of the tool can be seen at https://github.com/wgmao/EPIANN.

  To amplify the positive samples in the training set to 20 times to achieve class balance, we used this tool.
  

- sequence_processing.py

  Perform pre-processing of DNA sequences:

  1. Transform the enhancer and promoter gene sequences into word sequences (6-mers), marking a word as "NULL" if it contains "N".
  2. Create a dictionary with 4^6+1 words.
  3. Transform each gene sequence into a list of dictionary-compliant word indexes (each word has its own unique index).
  4. save the dna2vec embeddings into .npz files
  
- embedding_matrix.npy

    The weight of the embedding layer was calculated using Ng's pre-trained DNA vector (2017).
    
- model.py

    It contains the implementation of our proposed EPI-Trans model

- transformer.py

    It contains the implementation of the transformer module.

- train.py

  Perform model training.

- test.py

  Evaluate the performance of the model.

- requirments.txt
  
  The versions of the other used software libraries and frameworks.
     
You can find the weight of the model mentioned in our paper under the directory ./models

Directory|Content 
  ---|---
  models/Specific/| the weights of the specific models of the six cell lines.
  models/General/| the weights of the genral model.
  models/Best/| the weights of the best model of the six cell lines.
  
References:

  Mao, W. et al. (2017) Modeling Enhancer-Promoter Interactions with Attention-Based Neural Networks. bioRxiv, 219667.

  Ng, P. (2017) dna2vec: Consistent vector representations of variable-length k-mers. arXiv:1701.06279.
