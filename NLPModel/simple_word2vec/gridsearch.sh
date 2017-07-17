# typical output
# Epoch    1 Step   450327: lr = 0.153 loss =   5.37 words/sec =    11204
# Eval  100/8491 accuracy =  1.2%
# Epoch    2 Step   901197: lr = 0.106 loss =   4.14 words/sec =    12384
# Eval  222/8491 accuracy =  2.6%
# Epoch    3 Step  1351316: lr = 0.059 loss =   5.18 words/sec =      408
# Eval  375/8491 accuracy =  4.4%

# embedding_size: 10 - 400
# learning_rate: 0.0001 - 10
# batch_size: 4 - 512
# window_size: 1 - 20

#for((ws=5;ws<20;ws++)); do
#    for((bs=6;bs<50;bs++)); do
#        for((es=10;es<40;es++)); do

#        done
#    done
#done

# change step to 2, change learning rate from 0.2-->1
for((ws=5;ws<21;ws++)); do
    for((bs=5;bs<512;bs=bs+2)); do
        for((es=10;es<400;es=es+2)); do
            # echo hyperparameters to res.txt
            hyperDesc="Hyperparameters: ws_$ws bs_$bs es_$es"
            echo $ws 
            echo $bs 
            echo $es
            echo $hyperDesc
            echo $hyperDesc >> res4.txt
            python word2vec.py --train_data text8.small --eval_data questions-words.txt --save_path temp --embedding_size $es --batch_size $bs --window_size $ws | while read line; do
                echo $line
                echo $line >> res4.txt
            done
        done
    done
done
