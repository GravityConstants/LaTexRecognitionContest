# LaTexRecognitionContest
## Tools
- LaTex print GUI: https://quicklatex.com/
- LaTex print script: print-latex.py (Incomplete)
    - Print the formula.
        ```
        python print-latex.py '\frac{a}{b}'
        ```
    - Save the formula
        ```
        python print-latex.py '\forall x \in X, \quad \exists y \leq \epsilon' --file /tmp/test.png
        ```
- LaTex data set process
  ```
  python process.py '/tmp/data/training/TAL_OCR_FORMULA手写公式数据集/train.txt'
  ```