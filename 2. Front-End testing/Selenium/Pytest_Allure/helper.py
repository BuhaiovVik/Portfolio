from faker import Faker
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

fake = Faker()

# Locators
cross = "//button[@aria-label='prnux_close_minicart']"
home_decor = "//a[contains(.,'Home Decor and Accessories')]"
go_set = ("//img[@srcset='https://www.prada.com/content/dam/pradabkg_products/2/2SG/2SG008/0DCF0002"
          "/2SG008_0DC_F0002_SLF.jpg/_jcr_content/renditions/cq5dam.web.hebebed.600.600.jpg, "
          "https://www.prada.com/content/dam/pradabkg_products/2/2SG/2SG008/0DCF0002/2SG008_0DC_F0002_SLF.jpg"
          "/_jcr_content/renditions/cq5dam.web.hebebed.1200.1200.jpg 2x, "
          "https://www.prada.com/content/dam/pradabkg_products/2/2SG/2SG008/0DCF0002/2SG008_0DC_F0002_SLF.jpg"
          "/_jcr_content/renditions/cq5dam.web.hebebed.1800.1800.jpg 3x']")
check_out = "//button[contains(.,'Proceed to checkout')]"
check_box = ("/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/section[1]/div[5]/div[1]/div[1]/div["
             "1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/input[1]")
address_1 = ("/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/section[1]/div[5]/div[1]/div[1]/div["
             "1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/input[1]")
address_change = ("//body/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/section[1]/article[3]/div[1]/div[2]/div["
                  "1]/div[2]/div[1]/div[2]/button[1]")
mail_scroll = "/html[1]/body[1]/div[1]/div[3]/section[1]/div[1]/div[3]/div[1]/div[1]/div[2]/button[1]"
drop_down = """//select[@id='gigya-dropdown-43592239753641940']/option[text()="I'd rather not say"]"""
mail_confirm = "/html[1]/body[1]/div[1]/div[3]/section[1]/div[1]/div[3]/div[1]/div[1]/div[2]/button[1]/div[1]"
log_icon = "//span[@class='utils__icon pr-icon-new-logout']"
address_dd = "//a[@href='/us/en/logged-area.html?section=personal-information']"
address_title = "Logged Area | PRADA"
confirm = ("//body/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/section[1]/div[5]/div[1]/div[1]/div[1]/div["
           "3]/button[1]")
ship_address = "(//p[@class='card-address'])[1]"
bill_address = "(//p[@class='card-address'])[2]"
confirm_2 = "(//button[@type='button'][contains(.,'Confirm')])[7]"
state_dd = ("/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/section[1]/div[5]/div[1]/div[1]/div["
            "1]/div[2]/div[1]/div[3]/div[9]/div[1]/div[1]/input[1]")
re_edition = ("//a[@href='https://www.prada.com/us/en/womens/essentials/prada-re-edition/c/10103US'][contains(.,"
              "'Prada Re-Edition')]")
bag_img = ("/html[1]/body[1]/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/div[5]/ol[1]/li[1]/div[1]/article[1]/a[1]/div["
           "1]/div[1]/div[1]/picture[2]/img[1]")
show_more = "/html[1]/body[1]/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/div[4]/div[1]/a[1]/span[1]"
add_shop_bag = "(//div[contains(.,'Add to shopping bag')])[22]"
bag_mintgreen_button = "//*[@title='Mint Green']"
bag_mintgreen_img = ("//img[@srcset='https://www.prada.com/content/dam/pradabkg_products/1/1BH/1BH204/R064F0223"
                     "/1BH204_R064_F0223_V_V9L_SLF.jpg/_jcr_content/renditions/cq5dam.web.hebebed.600.600.jpg, "
                     "https://www.prada.com/content/dam/pradabkg_products/1/1BH/1BH204/R064F0223"
                     "/1BH204_R064_F0223_V_V9L_SLF.jpg/_jcr_content/renditions/cq5dam.web.hebebed.1200.1200.jpg 2x, "
                     "https://www.prada.com/content/dam/pradabkg_products/1/1BH/1BH204/R064F0223"
                     "/1BH204_R064_F0223_V_V9L_SLF.jpg/_jcr_content/renditions/cq5dam.web.hebebed.1800.1800.jpg 3x']")
bag_white_button = "//*[@title='Citron Yellow']"
bag_white_img = ("//img[@srcset='https://www.prada.com/content/dam/pradabkg_products/1/1BH/1BH204/R064F0322"
                 "/1BH204_R064_F0322_V_V9L_SLF.jpg/_jcr_content/renditions/cq5dam.web.hebebed.600.600.jpg, "
                 "https://www.prada.com/content/dam/pradabkg_products/1/1BH/1BH204/R064F0322"
                 "/1BH204_R064_F0322_V_V9L_SLF.jpg/_jcr_content/renditions/cq5dam.web.hebebed.1200.1200.jpg 2x, "
                 "https://www.prada.com/content/dam/pradabkg_products/1/1BH/1BH204/R064F0322"
                 "/1BH204_R064_F0322_V_V9L_SLF.jpg/_jcr_content/renditions/cq5dam.web.hebebed.1800.1800.jpg 3x']")
bag_orange_button = "//*[@title='Orange']"
bag_orange_img = ("//img[@srcset='https://www.prada.com/content/dam/pradabkg_products/1/1BH/1BH204/R064F0049"
                  "/1BH204_R064_F0049_V_V9L_SLF.jpg/_jcr_content/renditions/cq5dam.web.hebebed.600.600.jpg, "
                  "https://www.prada.com/content/dam/pradabkg_products/1/1BH/1BH204/R064F0049"
                  "/1BH204_R064_F0049_V_V9L_SLF.jpg/_jcr_content/renditions/cq5dam.web.hebebed.1200.1200.jpg 2x, "
                  "https://www.prada.com/content/dam/pradabkg_products/1/1BH/1BH204/R064F0049"
                  "/1BH204_R064_F0049_V_V9L_SLF.jpg/_jcr_content/renditions/cq5dam.web.hebebed.1800.1800.jpg 3x']")
go_img = ("//img[@srcset='https://www.prada.com/content/dam/pradabkg_products/2/2SG/2SG008/0DCF0002"
          "/2SG008_0DC_F0002_SLF.jpg/_jcr_content/renditions/cq5dam.web.hebebed.200.200.jpg, "
          "https://www.prada.com/content/dam/pradabkg_products/2/2SG/2SG008/0DCF0002/2SG008_0DC_F0002_SLF.jpg"
          "/_jcr_content/renditions/cq5dam.web.hebebed.400.400.jpg 2x, "
          "https://www.prada.com/content/dam/pradabkg_products/2/2SG/2SG008/0DCF0002/2SG008_0DC_F0002_SLF.jpg"
          "/_jcr_content/renditions/cq5dam.web.hebebed.600.600.jpg 3x']")
frag_img = ("/html[1]/body[1]/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/div[4]/ol[1]/li[1]/div[1]/article[1]/a["
            "1]/div[1]/div[1]/div[1]/picture[2]/img[1]")
frag_dd = "(//a[@href='https://www.prada.com/us/en/womens/fragrances/womens-fragrances/c/10464US'])[2]"
confirm_cart = "//button[contains(.,'Confirm')]"
proceed_checkout = ("/html[1]/body[1]/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div["
                    "2]/div[1]/button[1]")
confirm_checkout = "/html[1]/body[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/button[1]/div[1]"
confirm_address_checkout = ("/html[1]/body[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div["
                            "2]/div[1]/h2[1]")
cart_icon = "/html[1]/body[1]/div[3]/div[1]/header[1]/div[1]/div[1]/nav[1]/div[2]/div[5]/a[1]/span[1]"
card_name = (
    "/html[1]/body[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/form[1]/div["
    "1]/div[1]/div[1]/div[1]/input[1]")
card_lname = ("/html[1]/body[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/form["
              "1]/div[1]/div[2]/div[1]/div[1]/input[1]")
card_number = ("//div[@class='md:col-span-4 col-span-1 flex flex-row w-full input-container input-cc-number relative "
               "h-14 input-container-standard border border-black bg-white']")
card_mmyy = ("/html[1]/body[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/form["
             "1]/div[1]/div[2]/div[1]/div[1]/input[1]")
card_cvv = ("/html[1]/body[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/form["
            "1]/div[1]/div[2]/div[1]/div[1]/input[1]")
log_out_icon = "/html[1]/body[1]/div[3]/div[1]/header[1]/div[1]/div[1]/nav[1]/div[2]/div[3]/a[1]/span[1]"
log_out = "//button[@class='popup-logged-area__item'][contains(.,'Log out')]"
basket_del = ("//body/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/section[1]/article[3]/div[1]/div[2]/div[1]/div["
              "2]/div[1]/div[2]/button[2]/*[1]")
delete_confirm = ("/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/section[1]/div[11]/div[1]/div["
                  "1]/div[1]/div[2]/button[1]")

# Random data
phone = random.randint(2000000000, 5555555555)
date = fake.date()
mm_dd = date[5:7] + date[8:10]
f_name = fake.first_name()
l_name = fake.last_name()
company = fake.company()

# Addresses testing require real postal addresses, that why I can't use faker library and created this list
addresses = [
    "250 Rt 59, Airmont NY 10901",
    "141 Washington Ave Extension, Albany NY 12205",
    "13858 Rt 31 W, Albion NY 14411",
    "2055 Niagara Falls Blvd, Amherst NY 14228",
    "101 Sanford Farm Shpg Center, Amsterdam NY 12010",
    "297 Grant Avenue, Auburn NY 13021",
    "4133 Veterans Memorial Drive, Batavia NY 14020",
    "6265 Brockport Spencerport Rd, Brockport NY 14420",
    "5399 W Genesse St, Camillus NY 13031",
    "3191 County rd 10, Canandaigua NY 14424",
    "30 Catskill, Catskill NY 12414",
    "161 Centereach Mall, Centereach NY 11720",
    "3018 East Ave, Central Square NY 13036",
    "100 Thruway Plaza, Cheektowaga NY 14225",
    "8064 Brewerton Rd, Cicero NY 13039",
    "3949 Route 31, Clay NY 13041",
    "139 Merchant Place, Cobleskill NY 12043",
    "85 Crooked Hill Road, Commack NY 11725",
    "872 Route 13, Cortlandville NY 13045",
    "279 Troy Road, East Greenbush NY 12061",
    "2465 Hempstead Turnpike, East Meadow NY 11554",
    "6438 Basile Rowe, East Syracuse NY 13057",
    "901 Route 110, Farmingdale NY 11735",
    "2400 Route 9, Fishkill NY 12524",
    "10401 Bennett Road, Fredonia NY 14063",
    "1818 State Route 3, Fulton NY 13069",
    "4300 Lakeville Road, Geneseo NY 14454",
    "990 Route 5 20, Geneva NY 14456",
    "311 RT 9W, Glenmont NY 12077",
    "200 Dutch Meadows Ln, Glenville NY 12302",
    "100 Elm Ridge Center Dr, Greece NY 14626",
    "1549 Rt 9, Halfmoon NY 12065",
    "5360 Southwestern Blvd, Hamburg NY 14075",
    "103 North Caroline St, Herkimer NY 13350",
    "1000 State Route 36, Hornell NY 14843",
    "135 Fairgrounds Memorial Pkwy, Ithaca NY 14850",
    "2 Gannett Dr, Johnson City NY 13790",
    "233 5th Ave Ext, Johnstown NY 12095",
    "601 Frank Stottile Blvd, Kingston NY 12401",
    "350 E Fairmount Ave, Lakewood NY 14750",
    "4975 Transit Rd, Lancaster NY 14086",
    "579 Troy-Schenectady Road, Latham NY 12110",
    "5783 So Transit Road, Lockport NY 14094",
    "7155 State Rt 12 S, Lowville NY 13367",
    "425 Route 31, Macedon NY 14502",
    "3222 State Rt 11, Malone NY 12953",
    "200 Sunrise Mall, Massapequa NY 11758",
    "43 Stephenville St, Massena NY 13662",
    "750 Middle Country Road, Middle Island NY 11953",
    "470 Route 211 East, Middletown NY 10940",
    "3133 E Main St, Mohegan Lake NY 10547",
    "288 Larkin, Monroe NY 10950",
    "41 Anawana Lake Road, Monticello NY 12701",
    "4765 Commercial Drive, New Hartford NY 13413",
    "1201 Rt 300, Newburgh NY 12550",
    "515 Sawmill Road, West Haven CT 6516",
    "2473 Hackworth Road, Adamsville AL 35005",
    "630 Coonial Promenade Pkwy, Alabaster AL 35007",
    "2643 Hwy 280 West, Alexander City AL 35010",
    "540 West Bypass, Andalusia AL 36420",
    "5560 Mcclellan Blvd, Anniston AL 36206",
    "1450 No Brindlee Mtn Pkwy, Arab AL 35016",
    "1011 US Hwy 72 East, Athens AL 35611",
    "973 Gilbert Ferry Road Se, Attalla AL 35954",
    "1717 South College Street, Auburn AL 36830",
    "701 Mcmeans Ave, Bay Minette AL 36507",
    "750 Academy Drive, Bessemer AL 35022",
    "312 Palisades Blvd, Birmingham AL 35209",
    "1600 Montclair Rd, Birmingham AL 35210",
    "5919 Trussville Crossings Pkwy, Birmingham AL 35235",
    "9248 Parkway East, Birmingham AL 35206",
    "1972 Hwy 431, Boaz AL 35957",
    "10675 Hwy 5, Brent AL 35034",
    "2041 Douglas Avenue, Brewton AL 36426",
    "5100 Hwy 31, Calera AL 35040",
    "1916 Center Point Rd, Center Point AL 35215",
    "1950 W Main St, Centre AL 35960",
    "16077 Highway 280, Chelsea AL 35043",
    "1415 7Th Street South, Clanton AL 35045",
    "626 Olive Street Sw, Cullman AL 35055",
    "27520 Hwy 98, Daphne AL 36526",
    "2800 Spring Avn SW, Decatur AL 35603",
    "969 Us Hwy 80 West, Demopolis AL 36732",
    "3300 South Oates Street, Dothan AL 36301",
    "4310 Montgomery Hwy, Dothan AL 36303",
    "600 Boll Weevil Circle, Enterprise AL 36330",
    "3176 South Eufaula Avenue, Eufaula AL 36027",
    "7100 Aaron Aronov Drive, Fairfield AL 35064",
    "10040 County Road 48, Fairhope AL 36533",
    "3186 Hwy 171 North, Fayette AL 35555",
    "3100 Hough Rd, Florence AL 35630",
    "2200 South Mckenzie St, Foley AL 36535",
    "2001 Glenn Bldv Sw, Fort Payne AL 35968",
    "340 East Meighan Blvd, Gadsden AL 35903",
    "890 Odum Road, Gardendale AL 35071",
    "1608 W Magnolia Ave, Geneva AL 36340",
    "501 Willow Lane, Greenville AL 36037",
    "170 Fort Morgan Road, Gulf Shores AL 36542",
    "11697 US Hwy 431, Guntersville AL 35976",
    "42417 Hwy 195, Haleyville AL 35565",
    "1706 Military Street South, Hamilton AL 35570",
    "1201 Hwy 31 NW, Hartselle AL 35640",
    "209 Lakeshore Parkway, Homewood AL 35209",
    "2780 John Hawkins Pkwy, Hoover AL 35244",
    "5335 Hwy 280 South, Hoover AL 35242",
    "1007 Red Farmer Drive, Hueytown AL 35023",
    "2900 S Mem PkwyDrake Ave, Huntsville AL 35801",
    "11610 Memorial Pkwy South, Huntsville AL 35803",
    "2200 Sparkman Drive, Huntsville AL 35810",
    "330 Sutton Rd, Huntsville AL 35763",
    "6140A Univ Drive, Huntsville AL 35806",
    "4206 N College Ave, Jackson AL 36545",
    "1625 Pelham South, Jacksonville AL 36265",
    "1801 Hwy 78 East, Jasper AL 35501",
    "8551 Whitfield Ave, Leeds AL 35094",
    "8650 Madison Blvd, Madison AL 35758",
    "145 Kelley Blvd, Millbrook AL 36054",
    "1970 S University Blvd, Mobile AL 36609",
    "6350 Cottage Hill Road, Mobile AL 36609",
    "101 South Beltline Highway, Mobile AL 36606",
    "2500 Dawes Road, Mobile AL 36695",
    "5245 Rangeline Service Rd, Mobile AL 36619",
    "685 Schillinger Rd, Mobile AL 36695",
    "3371 S Alabama Ave, Monroeville AL 36460",
    "10710 Chantilly Pkwy, Montgomery AL 36117",
    "3801 Eastern Blvd, Montgomery AL 36116",
    "6495 Atlanta Hwy, Montgomery AL 36117",
    "851 Ann St, Montgomery AL 36107",
    "15445 Highway 24, Moulton AL 35650",
    "517 West Avalon Ave, Muscle Shoals AL 35661",
    "5710 Mcfarland Blvd, Northport AL 35476",
    "2453 2Nd Avenue East, Oneonta AL 35121",
    "2900 Pepperrell Pkwy, Opelika AL 36801",
    "92 Plaza Lane, Oxford AL 36203",
    "1537 Hwy 231 South, Ozark AL 36360",
    "2181 Pelham Pkwy, Pelham AL 35124",
    "165 Vaughan Ln, Pell City AL 35125",
    "3700 Hwy 280-431 N, Phenix City AL 36867",
    "1903 Cobbs Ford Rd, Prattville AL 36066",
    "4180 Us Hwy 431, Roanoke AL 36274",
    "13675 Hwy 43, Russellville AL 35653",
    "1095 Industrial Pkwy, Saraland AL 36571",
    "24833 Johnt Reidprkw, Scottsboro AL 35768",
    "1501 Hwy 14 East, Selma AL 36703",
    "7855 Moffett Rd, Semmes AL 36575",
    "150 Springville Station Blvd, Springville AL 35146",
    "690 Hwy 78, Sumiton AL 35148",
    "41301 US Hwy 280, Sylacauga AL 35150",
    "214 Haynes Street, Talladega AL 35160",
    "1300 Gilmer Ave, Tallassee AL 36078",
    "34301 Hwy 43, Thomasville AL 36784",
    "1420 Us 231 South, Troy AL 36081",
    "1501 Skyland Blvd E, Tuscaloosa AL 35405",
    "3501 20th Av, Valley AL 36854",
    "1300 Montgomery Highway, Vestavia Hills AL 35216",
    "4538 Us Hwy 231, Wetumpka AL 36092",
    "2575 Us Hwy 43, Winfield AL 35594",
    "3734 DELMAS TER, LOS ANGELES CA 90034",
    "860 VIA DE LA PAZ, PACIFIC PALISADES CA 90272",
    "2601 GARNET AVE, SAN DIEGO CA 92109",
    "809 LAUREL ST, SAN CARLOS CA 94070",
    "75 BUENA VISTA AVE, SAN FRANCISCO CA 94117",
    "429 N GRANT ST, STOCKTON CA 95202",
    "21581 PHOENIX LAKE RD, SONORA CA 95370",
    "1401 JEFFREY LN, PLACERVILLE CA 95667",
    "4327 PALM AVE, SACRAMENTO CA 95842",
    "552 S CANAL ST, HOLYOKE MA 01040",
    "2 CRESCENT RD, LONGMEADOW MA 01106",
    "1 BEACON CIR, SPRINGFIELD MA 01119",
    "34 RIVER RD, SUNDERLAND MA 01375",
    "700 PEARL ST, FITCHBURG MA 01420",
    "16A MAYBERRY DR, WESTBOROUGH MA 01581",
    "1 DALTON AVE, HAVERHILL MA 01835",
    "102 GAINSBOROUGH ST, BOSTON MA 02115",
    "913 MASSACHUSETTS AVE, BOSTON MA 02118",
    "801 BEECH ST, GIBSONIA PA 15044",
    "6301 BEIGHLEY RD, NEW KENSINGTON PA 15068",
    "701 BROWNSVILLE RD, PITTSBURGH PA 15210",
    "2 BROADWAY ST, MEYERSDALE PA 15552",
    "301 MCDOWELL RD, LIGONIER PA 15658",
    "400 MARWOOD RD, CABOT PA 16023",
    "2000 N HERMITAGE RD, HERMITAGE PA 16148",
    "11320 SAYBROOK RD, MEADVILLE PA 16335",
    "1301 S 10TH ST, ALTOONA PA 16602"
]

# Random addresses dictionary based
address = addresses[random.randint(0, 182)]
zip_code = address[-5:]
add = ""
for char in address:
    if char == ",":
        break
    add += char
city = address[len(add) + 2: -9]
state = address[-8: -6]

# New address generation
address_new = addresses[random.randint(0, 182)]
zip_code_new = address[-5:]
add_new = ""
for char in address:
    if char == ",":
        break
    add_new += char
city_new = address[len(add) + 2: -9]
state_new = address[-8: -6]

# Dictionary with XPATH locators for each state
us_abb = {
    'AL': "(//li[contains(., 'Alabama')])[3]",
    'AK': "(//li[contains(., 'Alaska')])[3]",
    'AZ': "(//li[contains(., 'Arizona')])[3]",
    'AR': "(//li[contains(., 'Arkansas')])[3]",
    'CA': "(//li[contains(., 'California')])[3]",
    'CO': "(//li[contains(., 'Colorado')])[3]",
    'CT': "(//li[contains(., 'Connecticut')])[3]",
    'DE': "(//li[contains(., 'Delaware')])[3]",
    'FL': "(//li[contains(., 'Florida')])[3]",
    'GA': "(//li[contains(., 'Georgia')])[3]",
    'HI': "(//li[contains(., 'Hawaii')])[3]",
    'ID': "(//li[contains(., 'Idaho')])[3]",
    'IL': "(//li[contains(., 'Illinois')])[3]",
    'IN': "(//li[contains(., 'Indiana')])[3]",
    'IA': "(//li[contains(., 'Iowa')])[3]",
    'KS': "(//li[contains(., 'Kansas')])[3]",
    'KY': "(//li[contains(., 'Kentucky')])[3]",
    'LA': "(//li[contains(., 'Louisiana')])[3]",
    'ME': "(//li[contains(., 'Maine')])[3]",
    'MD': "(//li[contains(., 'Maryland')])[3]",
    'MA': "(//li[contains(., 'Massachusetts')])[3]",
    'MI': "(//li[contains(., 'Michigan')])[3]",
    'MN': "(//li[contains(., 'Minnesota')])[3]",
    'MS': "(//li[contains(., 'Mississippi')])[3]",
    'MO': "(//li[contains(., 'Missouri')])[3]",
    'MT': "(//li[contains(., 'Montana')])[3]",
    'NE': "(//li[contains(., 'Nebraska')])[3]",
    'NV': "(//li[contains(., 'Nevada')])[3]",
    'NH': "(//li[contains(., 'New Hampshire')])[3]",
    'NJ': "(//li[contains(., 'New Jersey')])[3]",
    'NM': "(//li[contains(., 'New Mexico')])[3]",
    'NY': "(//li[contains(., 'New York')])[3]",
    'NC': "(//li[contains(., 'North Carolina')])[3]",
    'ND': "(//li[contains(., 'North Dakota')])[3]",
    'OH': "(//li[contains(., 'Ohio')])[3]",
    'OK': "(//li[contains(., 'Oklahoma')])[3]",
    'OR': "(//li[contains(., 'Oregon')])[3]",
    'PA': "(//li[contains(., 'Pennsylvania')])[3]",
    'RI': "(//li[contains(., 'Rhode Island')])[3]",
    'SC': "(//li[contains(., 'South Carolina')])[3]",
    'SD': "(//li[contains(., 'South Dakota')])[3]",
    'TN': "(//li[contains(., 'Tennessee')])[3]",
    'TX': "(//li[contains(., 'Texas')])[3]",
    'UT': "(//li[contains(., 'Utah')])[3]",
    'VT': "(//li[contains(., 'Vermont')])[3]",
    'VA': "(//li[contains(., 'Virginia')])[3]",
    'WA': "(//li[contains(., 'Washington')])[3]",
    'WV': "(//li[contains(., 'West Virginia')])[3]",
    'WI': "(//li[contains(., 'Wisconsin')])[3]",
    'WY': "(//li[contains(., 'Wyoming')])[3]",
}

# XPATH for current state
state_city = us_abb.get(state)
state_city_new = us_abb.get(state)


# Login
def login(driver):
    wait = WebDriverWait(driver, 20)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text() = 'ACCEPT ALL']")))
    driver.find_element(By.XPATH, "//*[text() = 'ACCEPT ALL']").click()
    wait.until(EC.visibility_of_element_located((By.ID, "gigya-textbox-100719189608483120")))
    with open("email.txt", "r") as file:
        email_text = file.read().strip()
    driver.find_element(By.ID, "gigya-textbox-100719189608483120").send_keys(email_text)
    driver.find_element(By.XPATH, "//input[contains(@value,'Next')]").click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@value,'Login')]")))
    with open("pass.txt", "r") as file:
        pass_text = file.read().strip()
    driver.find_element(By.ID, "gigya-password-83462624292152350").send_keys(pass_text)
    driver.find_element(By.XPATH, "//input[contains(@value,'Login')]").click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text() = "Start shopping "]')))
