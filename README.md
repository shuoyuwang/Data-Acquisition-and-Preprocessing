# Data collection:
1.In order to realize data collection, registration of Baidu Intelligent Cloud OCR recognition engine application, get its API Key and Secret Key.

<img width="398" alt="image" src="https://github.com/shuoyuwang/Data-Acquisition-and-Preprocessing/assets/59498813/5356249f-6ab0-4d88-a34a-88b77493bb5a">

<img width="398" alt="image" src="https://github.com/shuoyuwang/Data-Acquisition-and-Preprocessing/assets/59498813/0dd66eea-bcb7-41bd-82c7-a4cf6105565e">

2.Write access_token.py program to get access_token value by API Key and Secret Key.

<img width="398" alt="image" src="https://github.com/shuoyuwang/Data-Acquisition-and-Preprocessing/assets/59498813/2b7e7962-8f86-461f-8f72-b3594a0412d2">

3.Use access_token to call the VAT invoice recognition API in Baidu's text recognition technology, and write ocr_invoice.py code to extract the invoice

<img width="398" alt="image" src="https://github.com/shuoyuwang/Data-Acquisition-and-Preprocessing/assets/59498813/39c9c3e8-adb2-4c61-a465-383b8e5783b5">

4.Use access_token to call Baidu Universal Text Recognition (High Precision Edition) technology API, write ocr_contract.py program to extract the contract. As Baidu OCR is not specifically used to identify the contract API, so choose the General Text Recognition. As the contract is a pdf file, different from the invoice, so you need to modify the parameters for the "pdf_file" to meet the read pdf document.

<img width="397" alt="image" src="https://github.com/shuoyuwang/Data-Acquisition-and-Preprocessing/assets/59498813/a2d06198-a3bf-44f3-ad32-ea8f9ad0fda8">

5.Use access_token to call the Baidu Universal Text Recognition (high precision version) technology API, write ocr_bills.py program to extract the bank current

<img width="398" alt="image" src="https://github.com/shuoyuwang/Data-Acquisition-and-Preprocessing/assets/59498813/3a793515-90ff-4db5-a964-14078c5e1efb">

6.Standard field extraction extraction of bank flow txt file using NLP technique.

<img width="397" alt="image" src="https://github.com/shuoyuwang/Data-Acquisition-and-Preprocessing/assets/59498813/b049b19f-d0e0-41ea-b458-4489a939d2b6">

<img width="398" alt="image" src="https://github.com/shuoyuwang/Data-Acquisition-and-Preprocessing/assets/59498813/e72aec63-95c6-42db-be86-7db5dbb58e29">

<img width="355" alt="image" src="https://github.com/shuoyuwang/Data-Acquisition-and-Preprocessing/assets/59498813/f1de661e-fa45-45c7-9086-2cf69e0a318f">

7.Save the NLP extraction results to a txt file for subsequent data preprocessing operations.

<img width="620" alt="image" src="https://github.com/shuoyuwang/Data-Acquisition-and-Preprocessing/assets/59498813/02a34f81-7c1a-4526-ada4-34e75a64410c">

# Data preprocessing

1.Execute oce_accuracy.py program to extract the fuzzy and imprecise part of the text with high accuracy.

<img width="334" alt="image" src="https://github.com/shuoyuwang/Data-Acquisition-and-Preprocessing/assets/59498813/f851f25d-abcf-47ac-b1dd-5751405482eb">

Result：

<img width="398" alt="image" src="https://github.com/shuoyuwang/Data-Acquisition-and-Preprocessing/assets/59498813/feceadf3-d54a-4340-886b-c76b421db0c3">

2.Based on the NLP results and oce_accuracy on the final data identified are entered into the excel sheet separately.


<img width="397" alt="image" src="https://github.com/shuoyuwang/Data-Acquisition-and-Preprocessing/assets/59498813/237128a4-ee27-4696-bfb6-29361b22c48f">

<img width="398" alt="image" src="https://github.com/shuoyuwang/Data-Acquisition-and-Preprocessing/assets/59498813/877faa4c-3b47-4b94-aa4e-32f896612642">

<img width="293" alt="image" src="https://github.com/shuoyuwang/Data-Acquisition-and-Preprocessing/assets/59498813/f3bb83d0-6e3e-4de5-813c-f388ca5d7f7d">

# Data integration

1.Based on excel file, write Creat_mysql.py program to implement the creation of database, create 7 tables and store data from excel into database.

<img width="398" alt="image" src="https://github.com/shuoyuwang/Data-Acquisition-and-Preprocessing/assets/59498813/bb794124-2146-404b-b588-76b9a5e13de4">

<img width="398" alt="image" src="https://github.com/shuoyuwang/Data-Acquisition-and-Preprocessing/assets/59498813/0f68b294-fb0c-4ad0-b077-450e34f3a32f">

2.By writing a program that enables calculations to be performed on the stored data

(a) Total revenue, total net profit of the firm for each year;

<img width="214" alt="image" src="https://github.com/shuoyuwang/Data-Acquisition-and-Preprocessing/assets/59498813/3dc6f76c-2612-48a9-88e1-1a075e7e7856">

(b) Support for individual requirements.

In the program to leave a part of the sql statement, the user can according to the need to achieve the function of writing sql statements to achieve personalized needs.

<img width="360" alt="image" src="https://github.com/shuoyuwang/Data-Acquisition-and-Preprocessing/assets/59498813/4129e913-b45f-415e-8a95-e6630b799da4">
