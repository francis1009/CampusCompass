from bs4 import BeautifulSoup
import requests
import mysql.connector
from mysql.connector import errorcode



#get all school links
#url_main = "https://www.moe.gov.sg/schoolfinder?journey=Secondary%20school"
#page2 = requests.get(url_main)
#soup2 = BeautifulSoup(page2.text, "html.parser")
#print(soup2)
#list_of_url = []
#school_links = soup2.find_all("a", class_="moe-card hoverable cursor:pointer p:m m-b:m move-enter-done", target="_blank")
#all_a = soup2.find_all("div", class_= "moe-school-card-animation")
#print(all_a)



url_list_1 = ["https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=admiralty-secondary-school",
            "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=ahmad-ibrahim-secondary-school",
            "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=anderson-secondary-school",
            "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=ang-mo-kio-secondary-school",
            "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=anglican-high-school",
            "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=anglochinese-school-barker-road",
            "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=anglochinese-school-independent-secondary",
            "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=assumption-english-school",
            "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=assumption-pathway-school",
            "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=bartley-secondary-school",
            "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=beatty-secondary-school",
            "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=bedok-green-secondary-school",
            "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=bedok-south-secondary-school",
            "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=bedok-view-secondary-school",
            "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=bendemeer-secondary-school",
            "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=boon-lay-secondary-school",
            "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=bowen-secondary-school",
            "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=broadrick-secondary-school",
            "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=bukit-batok-secondary-school",
            "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=bukit-merah-secondary-school",
            ]

url_list_2 = ["https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=bukit-panjang-govt-high-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=bukit-view-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=canberra-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=catholic-high-school-secondary",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=cedar-girls-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=changkat-changi-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=chij-katong-convent",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=chij-secondary-toa-payoh",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=chij-st-josephs-convent",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=chij-st-nicholas-girls-school-secondary",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=chij-st-theresas-convent",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=christ-church-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=chua-chu-kang-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=chung-cheng-high-school-main",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=chung-cheng-high-school-yishun",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=clementi-town-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=commonwealth-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=compassvale-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=crescent-girls-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=crest-secondary-school",]

url_list_3 = ["https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=damai-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=deyi-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=dunearn-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=dunman-high-school-secondary",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=dunman-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=east-spring-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=edgefield-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=evergreen-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=fairfield-methodist-school-secondary",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=fuchun-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=fuhua-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=gan-eng-seng-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=geylang-methodist-school-secondary",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=greendale-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=greenridge-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=guangyang-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=hai-sing-catholic-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=hillgrove-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=holy-innocents-high-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=hougang-secondary-school"]

url_list_4 = ["https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=hua-yi-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=hwa-chong-institution-secondary",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=junyuan-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=jurong-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=jurong-west-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=jurongville-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=juying-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=kent-ridge-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=kranji-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=kuo-chuan-presbyterian-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=loyang-view-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=manjusri-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=maris-stella-high-school-secondary",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=marsiling-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=mayflower-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=meridian-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=methodist-girls-school-secondary",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=montfort-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=nan-chiau-high-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=nan-hua-high-school"]

url_list_5 = ["https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=nanyang-girls-high-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=national-junior-college-secondary",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=naval-base-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=new-town-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=ngee-ann-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=north-vista-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=northbrooks-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=northland-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=northlight-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=nus-high-school-of-mathematics-and-science",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=orchid-park-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=outram-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=pasir-ris-crest-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=pasir-ris-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=paya-lebar-methodist-girls-school-secondary",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=pei-hwa-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=peicai-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=peirce-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=presbyterian-high-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=punggol-secondary-school"]

url_list_6 = ["https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=queenstown-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=queensway-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=raffles-girls-school-secondary",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=raffles-institution-secondary",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=regent-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=river-valley-high-school-secondary",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=riverside-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=school-of-science-and-technology-singapore",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=school-of-the-arts-singapore",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=sembawang-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=seng-kang-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=serangoon-garden-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=serangoon-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=singapore-chinese-girls-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=singapore-sports-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=spectra-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=springfield-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=st-andrews-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=st-anthonys-canossian-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=st-gabriels-secondary-school"]

url_list_7 = ["https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=st-hildas-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=st-josephs-institution-secondary",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=st-margarets-school-secondary",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=st-patricks-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=swiss-cottage-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=tampines-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=tanjong-katong-girls-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=tanjong-katong-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=temasek-junior-college-secondary",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=temasek-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=unity-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=victoria-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=west-spring-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=westwood-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=whitley-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=woodgrove-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=woodlands-ring-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=woodlands-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=xinmin-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=yio-chu-kang-secondary-school"]

url_list_8 = ["https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=yishun-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=yishun-town-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=yuan-ching-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=yuhua-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=yusof-ishak-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=yuying-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=zhenghua-secondary-school",
              "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=zhonghua-secondary-school",]

big_url_list = [url_list_1, url_list_2, url_list_3, url_list_4, url_list_5, url_list_6, url_list_7, url_list_8]
#set school to be scraped
#url = "https://www.moe.gov.sg/schoolfinder/schooldetail?schoolname=anglochinese-school-independent-secondary",
for url_list in big_url_list:
    for url in url_list:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        #school name
        school_name = soup.find("h1", class_="m-b:l")
        school_name = school_name.text.strip()

        #school region
        school_region_div = soup.find("div", class_="d:f fld:c")
        school_region = school_region_div.find("span")
        school_region = school_region.text.strip()
        #print(school_region)

        #school address and postal code
        school_address = soup.find("a", class_="ts:m")
        school_address = school_address.text.strip()
        school_address = school_address.split(",")
        school_address_name = school_address[0]
        school_postal_code = school_address[1].strip()
        #print(school_address_name)
        #print(school_postal_code)

        #school code
        school_code = soup.find("span", class_="fw:7")
        school_code = school_code.text.strip()
        #print(school_code)

        school_about = soup.find_all("span", class_="d:b c:grey-2")
        school_mode = school_about[0].text.strip()
        #print(school_mode)

        school_nature = school_about[1].text.strip()
        #print(school_nature)

        school_type = school_about[2].text.strip()
        #print(school_type)

        school_number = soup.find("span", class_="d:b c:grey-2 m-b:l")
        school_number = school_number.text.strip()
        #print(school_number)

        school_email = soup.find("a", class_="c:primary-1")
        school_email = school_email.text.strip()
        #print(school_email)

        link_list = soup.find_all("a", rel="noopener noreferrer", target="_blank")
        for a in link_list:
            if ".edu.sg" in a["href"]:
                school_website = a.text.strip()
        #print(school_website)
        #school_website = school_website[59].text.strip()
        #print(school_website)

        school_image_src = soup.find("div", class_="moe-card w:4xl p:xs m-r:2xl fls:0 m-b:l")
        school_image_link = school_image_src.find("img")
        school_image_link = "https://moe.gov.sg" + school_image_link["src"]  
        #print(school_image_link)

        #table1: general info of schools
        #headers: [school_code, school_name, school_region, school_address, school_postal_code, school_mode, school_nature, school_type, school_number, school_email, school_website]


        #data headers
        headers = soup.find_all("span", class_="moe-collapsible__heading")
        header_list_clean = []
        for header in headers:
            header_clean = header.text.strip()
            header_list_clean.append(header_clean)
        #print(header_list_clean)

        #PSLE admission scores
        contents = soup.find_all("div", class_="moe-collapsible__content")
        if "PSLE score range of 2022" in header_list_clean:
            index_PSLE = header_list_clean.index("PSLE score range of 2022")
            PSLE_score_data_headers = contents[index_PSLE].find_all("th")
            PSLE_score_data_headers_clean = []
            for header in PSLE_score_data_headers:
                header_clean = header.text.strip()
                PSLE_score_data_headers_clean.append(header_clean)
            #print(PSLE_score_data_headers_clean)
            affiliation_cats = PSLE_score_data_headers_clean[1:3]
            affiliation_cats = affiliation_cats.reverse()
            if len(PSLE_score_data_headers_clean) == 7:
                education_lvl_cats = PSLE_score_data_headers_clean[3:7]
            else:
                education_lvl_cats = PSLE_score_data_headers_clean[3:6]
            #print(affiliation_cats)
            #print(education_lvl_cats)
            PSLE_score_data = contents[0].find_all("td")
            PSLE_score_data_clean = []
            for data in PSLE_score_data:
                data_clean = data.text.strip()
                PSLE_score_data_clean.append(data_clean)
            #print(PSLE_score_data_clean)

        #table 2, PSLE admission scores
        #headers: [(express, affiliation), (express, non-affililated), (NA, affiliated), (NA,non-affiliated), (NT, affiliated), (NT, non-affiliated)]


        #Subjects
        if "Subjects offered" in header_list_clean:
            index_subject = header_list_clean.index("Subjects offered")
            subjects = contents[index_subject].find("ul", class_="moe-list")
            all_subjects = subjects.find_all("li")
            subjects_text = []
            for subject in all_subjects:
                subject_text = subject.text.strip()
                subjects_text.append(subject_text)
            #print(subjects_text)

        #table3, subjects
        #headers: [school_code, subject_offered]


        #Special Programmes
        if "Electives and programmes" in header_list_clean:
            index_elective = header_list_clean.index("Electives and programmes")
            divs = contents[index_elective].find_all("div")
            total_special_programmes = {}
            for div in divs:
                if div.find("span", class_="d:b ff:heading ts:l m-b:m fw:6 c:grey-1") != None:
                    title = div.find("span", class_="d:b ff:heading ts:l m-b:m fw:6 c:grey-1")
                    title_text = title.text.strip()
                    if div.find("span", class_="d:b ts:m m-b:m fw:7 c:grey-2") != None:
                        subtitle = div.find("span", class_="d:b ts:m m-b:m fw:7 c:grey-2")
                        subtitle_text = subtitle.text.strip()
                        list_item = []
                        #check for case where theres no list item
                        list_of_li = div.find_all("li")
                        #print(list_of_li)
                        for li in list_of_li:
                            li_text = li.text.strip()
                            list_item.append(li_text)
                        total_special_programmes[title_text] = {subtitle_text: list_item}
                    else:
                        list_item = []
                        list_of_li = div.find_all("li")
                        #print(list_of_li)
                        for li in list_of_li:
                            li_text = li.text.strip()
                            list_item.append(li_text)
                        total_special_programmes[title_text] = list_item

            #print(total_special_programmes)
                

        
        #special_programmes = contents[2].find_all("span", class_="d:b ff:heading ts:l m-b:m fw:6 c:grey-1")
        #print(special_programmes)
        #special_programmes_title = []
        #for title in special_programmes:
        #    title_text = title.text.strip()
        #    special_programmes_title.append(title_text)
        #special_programmes_subtitle = contents[2].find_all("span", class_="d:b ts:m m-b:m fw:7 c:grey-2")
        #special_programmes_subtitle_text = []
        #for subtitle in special_programmes_subtitle:
        #    subtitle_text = subtitle.text.strip()
        #    special_programmes_subtitle_text.append(subtitle_text)
        #special_programmes_list_item =  contents[2].find_all("li")
        #special_programmes_list_item_text = []
        #for list_item in special_programmes_list_item:
        #    list_item_text = list_item.text.strip()
        #    special_programmes_list_item_text.append(list_item_text)
        #print(special_programmes_title)
        #print(special_programmes_subtitle_text)
        #print(special_programmes_list_item_text)



        #DSA
        if "DSA talent areas offered in 2023" in header_list_clean:
            index_dsa = header_list_clean.index("DSA talent areas offered in 2023")
            dsa = contents[index_dsa].find("ul", class_="moe-list")
            all_dsa = dsa.find_all("li")
            dsa_text = []
            for dsa_area in all_dsa:
                dsa_text.append(dsa_area.text.strip())
            #print(dsa_text)



        #cca
        if "Co-Curricular Activities (CCAs)" in header_list_clean:
            index_cca = header_list_clean.index("Co-Curricular Activities (CCAs)")
            cca = contents[index_cca].find("ul", class_="moe-list")
            all_cca = cca.find_all("li")
            cca_text = []
            for cca_area in all_cca:
                cca_text.append(cca_area.text.strip())
            #print(cca_text)

        #special ed support
        if "Support for special educational needs" in header_list_clean:
            index_special_ed = header_list_clean.index("Support for special educational needs")
            special_ed_support = contents[index_special_ed].find("ul", class_="moe-list")
            all_special_ed_support = special_ed_support.find_all("li")
            special_ed_support_text = []
            for special_ed_support_area in all_special_ed_support:
                special_ed_support_text.append(special_ed_support_area.text.strip())
            #print(special_ed_support_text)

        #affiliations
        affiliation_status = False
        big_div = soup.find_all("td", class_ = "bd:0 desktop(p-t:xl) desktop(p-b:xl)")
        small_div = soup.find_all("span", class_="ff:heading ts:xl fw:6 c:grey-1")
        for i in small_div:
            if i.text.strip() == "Affiliations":
                affiliation_status = True
                schools = []
                school_divs = soup.find_all("span", class_="d:b m-b:s")
                for school in school_divs:
                    schools.append(school.text.strip())
        #print(schools)


        #connect to database
        try:
            cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='singaporeschools')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

        cursor = cnx.cursor()

        add_general_info = ("INSERT INTO GeneralDetails (school_code, school_name, school_region, school_address, school_postal_code, school_mode, school_nature, school_type, school_number, school_email, school_website, school_image_source) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        data_general_info = (school_code, school_name, school_region, school_address_name, school_postal_code, school_mode, school_nature, school_type, school_number, school_email, school_website, school_image_link)
        cursor.execute(add_general_info, data_general_info)
        cnx.commit()
        if "PSLE score range of 2022" in header_list_clean:
            if len(PSLE_score_data_headers_clean) == 7:
                add_PSLE_admission_scores_info = ("INSERT INTO PSLE_Score_Details (school_code, IP_Affiliation, IP_NonAffiliation, Express_Affiliation, Express_NonAffiliation, NA_Affiliation, NA_NonAffiliation, NT_Affiliation, NT_NonAffiliation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
                data_PSLE_admission_scores_info = (school_code, PSLE_score_data_clean[0], PSLE_score_data_clean[1], PSLE_score_data_clean[2], PSLE_score_data_clean[3], PSLE_score_data_clean[4], PSLE_score_data_clean[5], PSLE_score_data_clean[6], PSLE_score_data_clean[7])
            else:
                add_PSLE_admission_scores_info = ("INSERT INTO PSLE_Score_Details (school_code, IP_Affiliation, IP_NonAffiliation, Express_Affiliation, Express_NonAffiliation, NA_Affiliation, NA_NonAffiliation, NT_Affiliation, NT_NonAffiliation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
                data_PSLE_admission_scores_info = (school_code, "-", "-", PSLE_score_data_clean[0], PSLE_score_data_clean[1], PSLE_score_data_clean[2], PSLE_score_data_clean[3], PSLE_score_data_clean[4], PSLE_score_data_clean[5])
            cursor.execute(add_PSLE_admission_scores_info, data_PSLE_admission_scores_info)
            cnx.commit()
            

        if "Subjects offered" in header_list_clean:
            add_subject_info = ("INSERT INTO Subjects_Offered (school_code, subject_offered) VALUES (%s, %s)")
            for subject in subjects_text:
                data_subject_info = (school_code, subject)
                cursor.execute(add_subject_info, data_subject_info)
                cnx.commit()

        if "DSA talent areas offered in 2023" in header_list_clean:
            add_dsa_info = ("INSERT INTO dsa_opportunities (school_code, dsa_cca) VALUES (%s, %s)")
            for dsa in dsa_text:
                data_dsa_info = (school_code, dsa)
                cursor.execute(add_dsa_info, data_dsa_info)
                cnx.commit()

        if "Co-Curricular Activities (CCAs)" in header_list_clean:
            add_cca_info = ("INSERT INTO cca_offered (school_code, cca) VALUES (%s, %s)")
            for cca in cca_text:
                data_cca_info = (school_code, cca)
                cursor.execute(add_cca_info, data_cca_info)
                cnx.commit()

        if "Support for special educational needs" in header_list_clean:
            add_special_ed_support_info = ("INSERT INTO special_ed_support (school_code, support_scheme) VALUES (%s, %s)")
            for scheme in special_ed_support_text:
                data_special_ed_info = (school_code, scheme)
                cursor.execute(add_special_ed_support_info, data_special_ed_info)
                cnx.commit()

        if "Electives and programmes" in header_list_clean:
            add_special_programmes_info = ("INSERT INTO electives (school_code, elective_name, elective_sub_header, elective_sub_sub_header) VALUES (%s, %s, %s, %s)")
            for key in total_special_programmes:
                if type(total_special_programmes[key]) == dict:
                    for sub_key in total_special_programmes[key]:
                        for i in range(len(total_special_programmes[key][sub_key])):
                            data_special_programmes_info = (school_code, key, sub_key, total_special_programmes[key][sub_key][i])
                            cursor.execute(add_special_programmes_info, data_special_programmes_info)
                            cnx.commit()
                else:
                    for i in range(len(total_special_programmes[key])):
                        data_special_programmes_info = (school_code, key, "-", total_special_programmes[key][i])
                        cursor.execute(add_special_programmes_info, data_special_programmes_info)
                        cnx.commit()

        if affiliation_status == True:
            add_affiliated_schools_info = ("INSERT INTO affiliations (school_code, affiliated_school) VALUES (%s, %s)")
            for school in schools:
                data_affiliated_schools_info = (school_code, school)
                cursor.execute(add_affiliated_schools_info, data_affiliated_schools_info)
                cnx.commit()


        #cursor.close()
        #cnx.close()


