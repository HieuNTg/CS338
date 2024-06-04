#  Date Recognition in Products


## Describe:
  - Input: A image contains expiration date 
  - Output: Print the expiration date to the screen
<p align="center">
  <img  width="1024" alt="image" src="https://github.com/HieuNTg/Date-Recognition/assets/96096473/23da4d31-45d7-4824-96bd-3b2aa25b090f">
</p>


## Dataset:
- Date-Synth dataset: 128510 single images, taken day, month, year: 
    - Traning: 89957 images
    - Validation: 25702 images
    - Test: 12851
  
=> Train and perform the task of recognizing text from images.

- Products-Synth dataset: 11,860 single images taken directly of products with expiration dates visible:
    - Traning: 8300 images
    - Validation: 2371 images
    - Test: 1187

=> Train the model to recognize the area containing the expiration date, month, and year on the product.

## Pipline
   <p align="center">
     <img width="604" alt="image" src="https://github.com/HieuNTg/Date-Recognition/assets/96096473/b5c758ed-fcb5-4e10-a2c8-a71720b8865a">
    </p>


## Result
- Detect
      ![image](https://github.com/HieuNTg/Date-Recognition/assets/96096473/e3e831fa-b112-439f-8f3f-7ad5f7aa7345)

- Text Recognition
    <p align="center">
     <img align="center" width="325" alt="image" src="https://github.com/HieuNTg/Date-Recognition/assets/96096473/0c8f2223-ef85-43cc-a957-2865861b330a">
    </p>
        

## Instructions:
- Please git clone repository
- Install the necessary libraries
  ```shell
  pip install -r requirements.txt
  
- At the repository folder, run Terminal:
   ```shell
  streamlit run app.py
  
