from bs4 import BeautifulSoup
import csv
from urllib.request import urlopen


csv_file = open('full.csv','w', encoding='utf-8-sig')

csv_writer = csv.writer((csv_file), lineterminator ="\n")
csv_writer.writerow(['name','page_link', 'profile_image', 'budget', 'recommendations', 'description', 'cleaning_and_sanitising', 'physical_distancing', 'protective_equipment', 'screening', 'delivery_options', 'google_map_link', 'address', 'neighbourhood', 'hours_of_operation', 'cuisines', 'dining_style', 'dress_code', 'parking_details', 'public_transit','payment_options', 'executive_chef', 'entertainment', 'additional_information', 'gift_card_link', 'website', 'phone'])


url_prefix = 'https://www.opentable.com/london-restaurant-listings?covers=2&currentview=list&datetime=2021-07-01+22%3A00&latitude=51.51145&longitude=-0.136835&metroid=72&size=100&sort=Popularity&intersperseavailability=true&from='


url_suffix = 0

#LOOP THROUGH THE PAGES OF THE STARTING URL

def parse_website(url_prefix, url_suffix):
    
    for i in range(5):
        url = url_prefix + str(url_suffix)
        url_suffix = url_suffix + 100
        
        #SET NEW PAGE URL
        
        uClient = urlopen(url)
        page_html = uClient.read()
        uClient.close()
        soup = BeautifulSoup(page_html, "lxml")

        for restaurant in soup.findAll("li", {"class":"result content-section-list-row cf with-times"}):
            #NAME       
            try:
                name = restaurant.find('span', {'class':'rest-row-name-text'}).text
                print(name)
            except:
                name = None
        
        
            #RESTAURANT PAGE LINK
            try:
                page_link = restaurant.find('div', {'class':'rest-row-header-container'}).a['href']
                print(page_link)
            except:
                page_link = None
                
        
            #PROFILE IMAGE
            try:
                profile_image = restaurant.find('div', {'class':'rest-row-image'}).img['data-src']
                print(profile_image)
            except:
                profile_image = None
            
            
            new_uClient = urlopen(page_link)
            new_page_html = new_uClient.read()
            new_uClient.close()
            page_soup = BeautifulSoup(new_page_html, "html.parser")
            
                
            #Budget
            try:
                budget = page_soup.select('div._4a920df5:nth-of-type(2) span')[0].text
                print(budget)
            except:
                budget = None
                
        
            #Recommendations
            try:
                top_tag_container = page_soup.select('div._6e561df4')
                recommendation_tags = ''
                top_tags = top_tag_container[0].find_all('a')
                for i in range(len(top_tags)):
                    recommendation_tags = recommendation_tags + top_tags[i].get_text() + '\n'
                    
                recommendations = recommendation_tags.strip()
                print(recommendations)
        
            except:
                recommendations = None
                
        
            #Description
            try:
                description = page_soup.find('div', class_='_3c23fa05').text
                print(description)
            except:
                description = None
                
        
            #Cleaning & Sanitising
            try:
                cleaning_info = page_soup.find('span', string ='Cleaning & Sanitizing').find_next_sibling().find_all('li')
                cleaning_and_sanitising_holder = ''
                for i in range(len(cleaning_info)):
                    cleaning_and_sanitising_holder = cleaning_and_sanitising_holder + cleaning_info[i].get_text() + '\n'
                cleaning_and_sanitising = cleaning_and_sanitising_holder.strip()
                print(cleaning_and_sanitising)
            except:
                cleaning_and_sanitising = None
                
        
            #Physical Distancing
            try:
                physical_distancing_info = page_soup.find('span', string ='Physical Distancing').find_next_sibling().find_all('li')
                physical_distancing_holder = ''
                for i in range(len(physical_distancing_info)):
                    physical_distancing_holder = physical_distancing_holder + physical_distancing_info[i].get_text() + '\n'
                    physical_distancing = physical_distancing_holder.strip()
                print(physical_distancing)
            except:
                physical_distancing = None
                
        
            #Protective Equipment
            try:
                protective_equipment_info = page_soup.find('span', string ='Protective Equipment').find_next_sibling().find_all('li')
                protective_equipment_holder = ''
                for i in range(len(protective_equipment_info)):
                    protective_equipment_holder = protective_equipment_holder + protective_equipment_info[i].get_text() + '\n'
                    protective_equipment = protective_equipment_holder.strip()
                print(protective_equipment)
            except:
                protective_equipment = None
                
        
            #Screening
            try:
                screening_info = page_soup.find('span', string ='Screening').find_next_sibling().find_all('li')
                screening_holder = ''
                for i in range(len(screening_info)):
                    screening_holder = screening_holder + screening_info[i].get_text() + '\n'
                    screening = screening_holder.strip()
                print(screening)
            except:
                screening = None
                
        
            #Delivery Options
            try:
                hg = page_soup.select('a.c2033341')
                delivery_options_holder = ''
                for i in range(len(hg)):
                    delivery_options = delivery_options_holder + (hg[i])['href'] + '\n'
                    delivery_options = delivery_options_holder.strip()
                print(delivery_options)
            except:
                delivery_options = None
                
        
            #Google Map Link
            try:
                google_info = page_soup.find('div', class_='e9508c55')
                google_map_link = google_info.a['href']
                print(google_map_link)
            except:
                google_map_link = None
                
        
            #Address
            try:
                address_span = page_soup.select('.c3981cf8 ._3ddfcf5c span')
                address = address_span[0].get_text()
                print(address)
            except:
                address = None
                
        
            #Neighbourhood
            try:
                neighbourhood = page_soup.find('span', string ='Neighborhood').find_parent().find_next_sibling().get_text()
                print(neighbourhood)
            except:
                neighbourhood = None
                
        
            #Hours of Operation
            try:
                hours_of_operation = page_soup.find('span', string ='Hours of operation').find_parent().find_next_sibling().get_text()
                print(hours_of_operation)
            except:
                hours_of_operation = None
                
        
            #Cuisines
            try:
                cuisines = page_soup.find('span', string ='Cuisines').find_parent().find_next_sibling().get_text()
                print(cuisines)
            except:
                cuisines = None
                
        
            #Dining Style
            try:
                dining_style = page_soup.find('span', string ='Dining Style').find_parent().find_next_sibling().get_text()
                print(dining_style)
            except:
                dining_style = None
                
        
            #Dress Code
            try:
                dress_code = page_soup.find('span', string ='Dress code').find_parent().find_next_sibling().get_text()
                print(dress_code)
            except:
                dress_code = None
                
        
            #Parking Details
            try:
                parking_details = page_soup.find('span', string ='Parking details').find_parent().find_next_sibling().get_text()
                print(parking_details)
            except:
                parking_details = None
                
        
            #Public Transit
            try:
                public_transit = page_soup.find('span', string ='Public transit').find_parent().find_next_sibling().get_text()
                print(public_transit)
            except:
                public_transit = None
                
        
            #Payment Options
            try:
                payment_options = page_soup.find('span', string ='Payment options').find_parent().find_next_sibling().get_text()
                print(payment_options)
            except:
                payment_options = None
                
        
            #Executive Chef
            try:
                executive_chef = page_soup.find('span', string ='Executive chef').find_parent().find_next_sibling().get_text()
                print(executive_chef)
            except:
                executive_chef = None
                
        
            #Entertainment
            try:
                entertainment = page_soup.find('span', string ='Entertainment').find_parent().find_next_sibling().get_text()
                print(entertainment)
            except:
                entertainment = None
                
        
            #Additional Information
            try:
                additional_information = page_soup.find('span', string ='Additional').find_parent().find_next_sibling().get_text()
                print(additional_information)
            except:
                additional_information = None
                
        
            #Gift Card Link
            try:
                gift_card_link = page_soup.find('span', string ='Gift Card').find_parent().find_next_sibling().a['href']
                print(gift_card_link)
            except:
                gift_card_link = None
                
        
            #Website
            try:
                website = page_soup.find('span', string ='Website').find_parent().find_next_sibling().get_text()
                print(website)
            except:
                website = None
                
        
            #Phone
            try:
                phone = page_soup.find('span', string ='Phone number').find_parent().find_next_sibling().get_text()
                print(phone)
            except:
                phone = None
                
            csv_writer.writerow([name, page_link, profile_image, budget, recommendations, description, cleaning_and_sanitising, physical_distancing, protective_equipment, screening, delivery_options, google_map_link, address, neighbourhood, hours_of_operation, cuisines, dining_style, dress_code, parking_details, public_transit, payment_options, executive_chef, entertainment, additional_information, gift_card_link, website, phone])
            
            
parse_website(url_prefix, url_suffix)