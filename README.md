# hk-getSalariesTax

## 1. CMHK payslip 

Assuming there is no extra voluntary contribution on your salary...

**Use this python code to get these data in a generated csv file:**
- Year and Month of the payslip
- MPF Relevant Income (for calculating salaries tax!)
- MPF Employer Mandatory Contribution
- The final total amount received for that particular month (i.e. MPF Relevant Income - Contribution)

**How to use:**

Put your relevant payslips for the tax period in a folder. It is suggested to name them with the format 'yyyy-mm'.
Set your own working directing in the path (if applicable).
``` path = 'C:/Users/user/Jupyter Notebook/payslip' ```
and
``` folderpath = r"C:\Users\user\Jupyter Notebook\payslip" ```

Since the payslip pdf is encrypted by default, we will need to decrpyt it before reading it. Therefore, input your password here.
``` decrypt_pdf(filename, de_fname, 'password') ```

If you want, you may also change the output csv file name.
``` 
if not os.path.isfile('tax.csv'):
   tax.to_csv('tax.csv', header='column_names', index=False)
else: 
   tax.to_csv('tax.csv', mode='a', header=False, index=False) 
```

### Points to note
- The template(s) used to generate the csv are subject to changes over the years. You may refer to the template folder for reference and more details.
