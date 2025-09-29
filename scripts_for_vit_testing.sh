python finetune_StyleAdv_ViT.py --testset EuroSAT --finetune_epoch 0 --model VitSmall --checkpoint output/vit/best.pth --name finetune-with-ata-meta-tuning --n_shot 1

python finetune_StyleAdv_ViT.py --testset CropDisease --finetune_epoch 0 --model VitSmall --checkpoint output/vit/best.pth --name finetune-with-ata-meta-tuning --n_shot 1

python finetune_StyleAdv_ViT.py --testset ISIC --finetune_epoch 0 --model VitSmall --checkpoint output/vit/best.pth --name finetune-with-ata-meta-tuning --n_shot 1

python finetune_StyleAdv_ViT.py --testset ChestX --finetune_epoch 0 --model VitSmall --checkpoint output/vit/best.pth --name finetune-with-ata-meta-tuning --n_shot 1

python finetune_StyleAdv_ViT.py --testset EuroSAT --finetune_epoch 0 --model VitSmall --checkpoint output/vit5shot/best.pth --name finetune-with-ata-meta-tuning --n_shot 5

python finetune_StyleAdv_ViT.py --testset CropDisease --finetune_epoch 0 --model VitSmall --checkpoint output/vit5shot/best.pth --name finetune-with-ata-meta-tuning --n_shot 5

python finetune_StyleAdv_ViT.py --testset ISIC --finetune_epoch 0 --model VitSmall --checkpoint output/vit5shot/best.pth --name finetune-with-ata-meta-tuning --n_shot 5

python finetune_StyleAdv_ViT.py --testset ChestX --finetune_epoch 0 --model VitSmall --checkpoint output/vit5shot/best.pth --name finetune-with-ata-meta-tuning --n_shot 5
