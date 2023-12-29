import requests
from bs4 import BeautifulSoup
import json
import re

####################################################################################
## This Script Is only written to scrape Image from CFMOTO GLOBAL WEBSITE ###
## If no working means they've made changes on their source code ##
####################################################################################


def scrape_and_download_images1(url, download_folder,file_name):
    try:
        
        response = requests.get(url)
        response.raise_for_status()

        pagesourcecode = response.text

 
        soup = BeautifulSoup(pagesourcecode, 'html.parser')

        # Find the productgallerycomponent tag
        product_gallery_component_tag = soup.find('productgallerycomponent')

        if product_gallery_component_tag:
            # Extract the lpicturelist attribute value
            lpicturelist_value = product_gallery_component_tag.get('lpicturelist')

            if lpicturelist_value:
                # Load the JSON data
                gallery_data = json.loads(lpicturelist_value)

                # Extract image URLs from the JSON data
                image_urls = gallery_data.get('imageList', [])

                # Create a list to store download links
                download_links = []

                for i, src_link in enumerate(image_urls, start=1):
                    full_url = f"https://www.cfmoto.com{src_link}"
                    print(f"Image {i} Src: {full_url}")

                    # Append the download link to the list
                    download_links.append(full_url)

                # Download images
                for i, download_link in enumerate(download_links, start=1):
                    response = requests.get(download_link)

                    # Save the image to the specified folder
                    with open(f"{download_folder}/{file_name}{i}.jpg", 'wb') as f:
                        f.write(response.content)

                    print(f"Downloaded image {i}")

            else:
                print("lpicturelist attribute value not found in productgallerycomponent tag.")

        else:
            print("productgallerycomponent tag not found.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


def scrape_and_download_images2(url, download_folder,file_name):
    try:

        response = requests.get(url)
        response.raise_for_status()

        pagesourcecode = response.text


        soup = BeautifulSoup(pagesourcecode, 'html.parser')

        # Find the productgallerycomponent tag
        product_gallery_component_tag = soup.find('productgallerycomponent')
        
        if product_gallery_component_tag:
            # Extract the lpicturelist attribute value
            lpicturelist_value = product_gallery_component_tag.get('spicturelist')

            if lpicturelist_value:
                # Load the JSON data
                gallery_data = json.loads(lpicturelist_value)

                # Extract image URLs from the JSON data
                image_urls = gallery_data.get('imageList', [])

                # Create a list to store download links
                download_links = []

                for i, src_link in enumerate(image_urls, start=1):
                    full_url = f"https://www.cfmoto.com{src_link}"
                    print(f"Image {i} Src: {full_url}")

                    # Append the download link to the list
                    download_links.append(full_url)

                # Download images
                for i, download_link in enumerate(download_links, start=1):
                    response = requests.get(download_link)

                    # Save the image to the specified folder
                    with open(f"{download_folder}/{file_name}{i}.jpg", 'wb') as f:
                        f.write(response.content)

                    print(f"Downloaded image {i}")

            else:
                print("spicturelist attribute value not found in productgallerycomponent tag.")

        else:
            print("productgallerycomponent tag not found.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")




if __name__ == "__main__":
    #IMAGE BOTTOM SLIDER 1
    website_url = "https://www.cfmoto.com/global/motorcycles/papio/xo-papio-racer.html"
    # Folder to save downloaded images
    download_folder = 'C:/xampp/htdocs/cfmotomalaysia.com.my/image/XO PAPIO/bottom-slider1'
    file_name = "PAPIO_1"
    #============================================================================================#
    #IMAGE BOTTOM SLIDER 2
    website_url2 = "https://www.cfmoto.com/global/motorcycles/papio/xo-papio-racer.html"
    # Folder to save downloaded images
    download_folder2 = 'C:/xampp/htdocs/cfmotomalaysia.com.my/image/XO PAPIO/bottom-slider2'
    file_name2 = "PAPIO_2"

    # Functions start
    scrape_and_download_images1(website_url, download_folder,file_name)  #IMAGE BOTTOM SLIDER 1
    scrape_and_download_images2(website_url2, download_folder2,file_name2)  #IMAGE BOTTOM SLIDER 2

