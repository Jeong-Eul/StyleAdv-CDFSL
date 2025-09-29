

python metatrain_StyleAdv_ViT.py --output output/vit5shot --dataset mini_imagenet --epoch 20 --lr 5e-5 --arch dino_small_patch16 --device cuda:0 --nSupport 5 --fp16

python metatrain_StyleAdv_ViT.py --output output/vit --dataset mini_imagenet --epoch 20 --lr 5e-5 --arch dino_small_patch16 --device cuda:0 --nSupport 1 --fp16

