

python finetune_StyleAdv_RN.py --testset CropDisease  --name StyleAdv-RN-1shot --train_aug --n_shot 5 --finetune_epoch 50 --resume_dir StyleAdv-RN-5shot --resume_epoch -1

python finetune_StyleAdv_RN.py --testset ChestX   --name StyleAdv-RN-1shot --train_aug --n_shot 5 --finetune_epoch 50 --resume_dir StyleAdv-RN-5shot --resume_epoch -1