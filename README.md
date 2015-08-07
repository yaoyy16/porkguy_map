# porkguy_map
豬肉俠公益地圖

## 安裝
- [安裝 Python 3.4](https://djangogirlstaipei.herokuapp.com/tutorials/installation/)
- 創建及切換虛擬環境

``` 
python -m venv VENV
```
``` 
VENV\Scripts\activate
```
- 安裝所有專案相關套件

```
pip install -r requirements.txt
```

## 輸入資料
```
python manage.py import_city
python manage.py import_fundget
python manage.py import_surplus
python manage.py import_lotterystore
python manage.py import_org
python manage.py add_prize_time
python manage.py add_project
python manage.py update_city
python manage.py update_org
python manage.py update_result
python manage.py update_store
python manage.py update_surplus
python manage.py remove_same
```
## 執行
```
python manage.py runserver
```
- 看結果 localhost:8000