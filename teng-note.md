- Count multiple lines:
```
Tengs-MacBook-Pro:LaTexRecognitionContest tengli$ cat /Users/tengli/Downloads/TAL_OCR_FORMULA手写公式数据集/train.txt | grep ' \\\\\\\\ '  | wc -l
   12380
```
- Get list of images with multiple lines
```
Tengs-MacBook-Pro:LaTexRecognitionContest tengli$ cat /Users/tengli/Downloads/TAL_OCR_FORMULA手写公式数据集/train.txt | grep ' \\\\\\\\ ' | jq '.ImageFile'
```
