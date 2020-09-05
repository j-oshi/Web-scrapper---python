# Web-scrapper---python
A simple web page scrapper which utilizes xpath expressions to get datas and save to files.
Repository includes source code and executable file (webscrapper.exe)

## How to run application
### Option 1: Clone repositiory and run
Clone repository && cd folder directory
In terminal, run with python <foldername>
  
### Option 2: Run executable
Download repository && extract webscrapper.exe
Click on webscrapper.exe to launch form.

## How to use
- Click on 'add scrapper' button to generate a scrap form.
- Select scrap form type and fill the form.
- Enter the xpath expression of element in dom to scrap.
- Click on the 'add to process' button to activate form and display the 'run scrapper' button.
- Click on the 'run scrapper' button to execute all added scrap processes and generate corresponding scrap data files. <br >

** To run new series of scrappers, remove unnecessary ones from process and new scrapper(s) to the scrap window in series of desired execution.

## Limits
A maximum of three scrap forms are allowed. Each form in the process can scrap a different page in series by using the single scrap form.<br>

single . single . single <br >

The forms can also be chained linked to perform three level scrapping (i.e., scrap child of child pages). Made possible by pairing a single scrap form with multi scrap form.<br >

** Multi page has a 'connect to' field to select previous scrapper to link to. <br >

single -> multi -> multi
