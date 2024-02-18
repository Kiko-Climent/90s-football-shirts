# 90's FOOTBALL SHIRTS
## Introduction
90's Football Shirts is a fictional site designed, developed and implemented with _Django_, _Python_, _HTML_, _CSS_, _JQuery_ and _JavaScript_. It is a vintage sports clothing store specializing in jerseys and tricots of football teams from the 90s.

The Deployed version of the site can be found here:

## Showcase
![](media/readme_media/responsive.png)

# UX

## Target Audience
The target audience of 90's Football Club extends beyond individuals interested solely in sports or football. We aim to appeal to those who have an interest in vintage fashion. Additionally, we seek to tap into consumers' nostalgia by revisiting prominent football figures and events from the 1990s

## User Stories

**EPIC: Registration and Profile**

***Site User:***
* As a _site user_ I can be able to _register_ a new account, so i have a _personal account and profile_
* As a _site user_ I can easily *log in* and _log out_ so i can have _access to my personal account_
* As a _site user_ I can _recover_ my password so i can _get access to my account again_
* As a _site user_ I can be able to _receive an email_ after submitting my registration form so i can _verify_ my submision was succesfully done
* As a _site user_ I can _edit_ my profile so i can _change_ payment and shipping information
* As a _Site User_ I can _have a personalized profile_ so that _i can have my orders, payment and shipping information_

**EPIC: Navitagtion**
* As a _site user_ I can easily _navegate_ through the different sections of the site so i can have a good _user experience_
* As a _site user_

**EPIC: Product**
* As a _site user_ I can have a _view of products_ so i can _select_ some to purchase
* As a _site user_ I can _add products_ to my shopping cart so i can _purchase them_
* As a _site user_ I can _select size and quantity_ so i can have a _good experience_ when buying products

**EPIC: Shopping Cart**
* As a _Site User_ I can _edit the items in my shopping cart_ so that _I don't have to come back to the product detail_
* As a _Site User_ I can _have a detailed view of prices_ so i can _be aware about shipping costs and discounts_
* As a _Site User_ i can have a detailed view of the products in my cart so _I know what I'm about to purchase_

**EPIC: Purchase**
* As a _Site User_ I can _add my shipping information_ so that _I make sure the items are shipped to the desired address_
* As a _Site User_ i can _add my payment details_ to purchase my products 
* As a _Site User_ I can _have a detailed list of items_ so that _I know exactly what I'm about to_ purchase

**EPIC: Contact**
* As a _site user_ I can have _access_ to a _contact form_ so i can _message_ the owner in case of an inquiry
* As a _site user_ I can _contact_ the owner concerning an _specific_ product
* As a _site user_ I can get a _confirmation email_ so im _aware_ that the submission was _succesfully sent_

**EPIC: Wishlist**
* As a _Site User_ I can _have a wishlist_ so that _I can have a list of items that i like_
* As a _Site User_ I can _add and remove items from my wishlist_ so that _i have a personalized list_

**EPIC: Ratings**
* As a _Site User_ i can _see a ratings field_ so _I know which are the favourite items from other users_
* As a _Site User_ I can rate a product so that _I can leave my feedback for other users_
* As a _Site User_ I can _update my ratings_ so that _I can reflect any changes in my experience_
...
...

### A list of detailed _Acceptance Criteria_ and _Tasks_ for each User Story can be found here:
![]()

## As Admin


### Strategy

_90's Football Club_ is a website that seeks to unite the passion for sports, specifically football, and vintage fashion, creating a time capsule to revisit great moments from football events during the golden era of the 90s.

## Architecture

## Database

<details>
<summary>Click to review the database schema: </summary>

![](media/readme_media/database_schema.jpg)

</details>

## Navigation
<details>
<summary>Click to review the navigation flow: </summary>

![](media/readme_media/flowchart_template.jpg)

</details>

## Design

<details>
<summary>Click to review the the wireframes
![]()
</details>

### Color Scheme

The colors used for the site design adopt a sober and simple style. I aimed to steer away from the typical white background to impart a retro and lo-fi touch, which I believe aligns with the _vintage_ concept of the page. Additionally, the muted blue tone complements perfectly with the landing page image.

### Typography

The font used for the development of the site was _Kanit_
![](media/readme_media/font.png)

...
# Features
## Homepage:
The landing page, where the user initially arrives, serves as the starting point of the website. On this page, users encounter various features with which they can interact
![]()

### Header and Navigation:
Logo site centered, with the search bar displaying on the left while the link to the shopping cart and the user's acount menu displaying on the right.
![](media/readme_media/logo_header_nav.png)

### Home Image and Call-to-Action:
![](media/readme_media/home_img_call_action.png)

### Discount and Shipping info tab:
![](media/readme_media/discount.png)
![](media/readme_media/info_shipping.png)

### Footer:
In the footer, visitors can access our Facebook page through a provided link, explore external links containing relevant information, and have the option to subscribe to our newsletter.
![]()

### My Account (User):
For users who are already registered and have an account, the user menu will display their benefits, such as having a user _Profile_ and their own _Wishlist_. The _Contact Form_ will be a benefit enjoyed by those users who are not registered as well.

![](media/readme_media/account_user.png)

### My Account (Admin):
Unlike the user menu for those who are registered, the admin menu provides a direct link to the _Management_ section where the admin can add new products to the store through a new interface.

![](media/readme_media/account_admin.png)

### Categories:

Users have the ability to navigate through the different categories of the page.

- In the *All Products* section, users can access all the products in the store, and they will be able to sort them by _Price_ or _Rating._

- *Clubs:* Here, products in the store are organized by leagues, including the _Premier League, La Liga, Serie A, Bundesliga,_ and a general category including products from _Other leagues._

- _*National Teams:*_ In this section, products belonging to national teams will be selected, with subcategories organized by continent.

- _Brands:_ Finally, users will also be able to view products sorted by sports _brands_ such as _Adidas, Nike, Umbro, Puma,_ etc.

![](media/readme_media/category_all_products.png)
![](media/readme_media/category_clubs.png)
![](media/readme_media/category_national.png)
![](media/readme_media/category_brands.png)

## Registrartion:
### Sign Up:
As mentioned earlier, and although it's possible to place orders for non-registered users, users should register to access their profiles and have control over the wishlist.

![](media/readme_media/sign_up.png)

### Log In page:
For already registered users, the form to access the user profile is straightforward. Username and password are the only required fields.

![](media/readme_media/log_in_page.png)

### Log In Success:
![](media/readme_media/log_in_success.png)

### Log Out:
![](media/readme_media/log_out.png)

## Products:
### All Products Page:
The view of all products includes a brief description of the item, which comprises the _Team Name, _Price, Sports Brand, Category or League_ in which the product is located, and the product's _Rating._

![](media/readme_media/all_products_page.png)

### Product Detail Page:
Selecting a desired item, we enter the product details, where a slightly longer description takes center stage. In addition to the fields mentioned earlier, the product includes a brief text describing the team, its achievements, and some interesting memorabilia.

_Size_ and _Quantity_ selection buttons are included, with a maximum of 5 units per item, as the allowed maximum.

At the bottom, users will find buttons to _Add the item_ to the _Shopping Cart_ and another one to navigate back to the complete list of products.

For registered users, the possibility to submit their own rating and add the product to their wishlist will also be available.

![](media/readme_media/product_detail.png)

### Product Detail Info:
![](media/readme_media/product_detail_info.png)

## Rating:
Upon clicking the _Ratings_ icon, the user will be shown a dropdown menu where they can enter their own rating

![](media/readme_media/rating.png)

## User's Wishlist:
Regarding the _Wishlist,_ Users can add items to the wishlist by clicking the Heart icon in the product description. The _Wishlist_ will display the products selected by the registered user in the product detail view. It's quite simple, including only the _Image, Team, Price,_ and two buttons—one to access the _Product Details_ again and another to _Remove_ it from the wishlist.

![](media/readme_media/wishlist.png)

## Shopping Cart:
The shopping cart will show all users the products they have previously added. Here, in addition to the image, the team's name, and the price, the selected size and quantity will be displayed, with the option to update or remove the quantity. In the same row, a column for the product subtotal will also be available.

![](media/readme_media/shopping_cart.png)

At the bottom, a cost _breakdown_ will be provided to the user. This includes the total price _before discount_, the amount to be _discounted (if applicable),_ as well as the _shipping costs (if applicable),_ and the _Grand Total,_ which is the amount the user needs to pay.

Finally, the user will find a button to return to the store and another one to proceed to the checkout page.

![](media/readme_media/amount_with_discount.png)

## Purchase:
On the Purchase page, we find a _summary_ of the user's cart at the top right. Meanwhile, on the left side, there is a form where the user will enter the _shipping details_ for the products about to be purchased. Just below, there is a field to enter _credit card information,_ as well as two buttons—one to _proceed_ with the payment and another to go _back to the cart_ in case any modifications are desired.

![](media/readme_media/purchase.png)
![](media/readme_media/shipping_details.png)
![](media/readme_media/products_resume.png)
![](media/readme_media/payment_information.png)

### Purchase-Success:
After the payment has been processed, the user will be redirected to the _Purchase Success_ page. In addition to a _confirmation message_ at the top, the _details_ related to the purchase will be displayed. A _Confirmation email_ will also be sent to the email address provided by the user earlier.

![](media/readme_media/purchase_success.png)
![](media/readme_media/order_confirmation_email.png)

## Profile:
### User's Profile:
The user profile consists of 2 sections, the first one with the _shipping details_ of the users that can be modified if the user wishes, and another section where the _Previous Orders_ will be stored.

![](/media/readme_media/users_profile.png)

## Contact
### Contact Form:
The _Contact form,_ available in the dropdown menu of the _accounts icon,_ is accessible to _all users,_ whether registered or not. In it, the fields to provide a response are mandatory. As for the _Subject,_ the user can choose between _General Inquiry_ or _Product._ Another dropdown menu that includes a list of all the products in the store will also be provided to ensure a good experience for both the admin and the user. In the _Message_ field, the user can explain the inquiry to the administrator.

![](/media/readme_media/contact_form.png)

### Contact Success
Once the fields have been filled out successfully, a confirmation message as well as an email will be provided to the user.

![](/media/readme_media/contact_success.png)

## Management:
The page administrator will have the ability to create new content for the page, as well as edit or delete existing content.

In the "accounts" icon, only the authenticated administrator will see a link labeled "Management," which will redirect them to the page for uploading new products to the store.
### Add New Product:
The form for _adding new products_ to the store includes all the fields that will later be displayed in the product _description_ within the _Product Detail_ page.
![](/media/readme_media/add_product.png)

### Edit / Delete Product:
Within the Product Detail page, if the authenticated user is the administrator, a new field will be displayed in the description where they can update or delete the product. Both links are also avilable from the _All Products_ page.

![](/media/readme_media/delete_product.png)
![](/media/readme_media/edit_product.png)
![](media/readme_media/all_products_management.png)


...

# Testing
## Manual Testing

### Home / Landing Page
| Feature | Test | Expected Result | Result |
| -------------| ----- | ----- | :----: |
| 90'S FOOTBALL SHIRTS | Click on Logo in Homepage | redirects user to home page | Pass |
| Navbar links | Click on Navigation Links | Redirects user to selected page | Pass |
| All Products | Click on All Products | Dropdown menu with the three categories | Pass |
| By Price | Click on By Price | Sort the products by price (lower to higher) | Pass |
| By Ratings | Click on By Price | Sort the products by rating (higher to lower) | Pass |
| All Products (Subcategory) | Click on All Products | Shows all the products in store | Pass |
| Clubs | Click on Clubs | Dropdown menu with the different leagues | Pass |
| Select league | Click on each league | Sort the products corresponding to the selected league | Pass |
| National Teams | Click on National Teams | Dropdown menu with the different continents | Pass |
| Select Continent | Click on each continent | Sort the products corresponding to the selected continent | Pass |
| Brands | Click on Brands | Dropdown menu with the different brands | Pass |
| Select Brand | Click on each brand | Sort the products by brands | Pass |
| Go to Shop | Click on Go to Shop Button | Shows all the products in store | Pass |
| Facebook icon | click on facebook icon | redirects user to facebook page |  Pass |
| Some Nostalgia (External Links) | click on the links | redirects the user to the selected external link | Pass |
| Sign up for our newsletter | click on Sign up for our newsletter | redirects user Sign up for our newsletter page |  Pass |
| Mailchimp logo | Click on Mailchimp logo | redirects user to Mailchimp homepage | Pass |
| Privacy policy | click on privacy policy | redirects user to privacy policy|  Pass |
| Search | Using the search box | Entering a search returns expected result  |  Pass |
| Search no results | Blank field | Entering a no results search returns error message and shows all products  |  Pass |
| My Account | Click on My Account | Dropdownn menu with 3 categories for the unlogged users | Pass |
| Register | Click on Register | Redirects user to sign up form | Pass |
| Log in | Click on Log in | Redirects user to log in page | Pass |
| Contact | Clic on Contact | Redirects user to contact form | Pass |
| Shopping Cart | Clic on Shopping Cart icon | Redirects user to Shopping Cart | Pass |

### Footer
| Feature | Test  | Expected Result | Result |
| -------------| ----- | ----- | :----: |
| External Links | Click on any external links | Open links in a new tab | Pass |
| Facebook Link | Click on facebok icon | Open Facebook page in a new tab | Pass |
| Newsletter | Insert email address to sign up | Register success | Pass |
| Newsletter | Insert blank field | This field is required | Pass |
| Newsletter | Insert existing email | Already subscribed | Pass |


### USER:

### Register
| Feature | Test | Expected Result | Result |
| -------------| ----- | ----- | :----: |
| Sign up form | Fill all the fields correctly | Verification email sent to user / Info Toast | Pass |
| Confirm e-mail adress | Click on Confirm | Account created / Success Toast | Pass |
| Sign up form | Leave some fields | Alerts user about it | Pass |
| Sign up form | Different email confirmation field | Alerts user about it | Pass |
| Sign up form | Different password confirmation | Alerts user about it | Pass |

### Log in
| Feature | Test | Expected Result | Result |
| -------------| ----- | ----- | :----: |
| Log in page | Introduced correctly both usernae and password | Succesfully logged in / Success Toast | Pass |
| Log in page | Invalid usernae or password | Alerts user abou it | Pass |

### Contact
| Feature | Test | Expected Result | Result |
| -------------| ----- | ----- | :----: |
| Contact Form | Fill all the fields correctly | Email confirmation sent / Success Toast | Pass |
| Contact Form | Leave some fields | Alerts user about it | Pass |
| Subject Type | Dropdown Menu | Select General or Product Inquiry | Pass |
| Product | Dropdown Menu | Select a product from the shop | Pass |

### My Profile
| Feature | Test | Expected Result | Result |
| -------------| ----- | ----- | :----: |
| My Profile | Once logged in click on My profile | Redirects to user's profile | Pass |
| User's Profile | Once logged in click on My profile | Shows Shipping Details and Past Orders | Pass |
| Update Profile | Click on Update Profile after editing details | Updates Shipping info | Pass |
| Past Orders | Click on Order Number | Redirects to Purchase Success from selected order / Info Toast | Pass |

### My Wishlist
| Feature | Test | Expected Result | Result |
| -------------| ----- | ----- | :----: |
| My Wishlist |  Once logged in click on My Wishlist | Redirects to user's wishlist | Pass |
| User's Profile | Once logged in click on My Wishliste | Shows a list of wished items from user | Pass |
| Remove from Wishlist | Click on Remove | Product removed from wishlist / Success Toast | Pass |
| Product Details | Clic on Details | Redirect to product details | Pass |

### Log out
| Feature | Test | Expected Result | Result |
| -------------| ----- | ----- | :----: |
| Log out | Click on Log out | Redirects user to Sign Out page | Pass |
| Sign out page | Click on Cancel | Redirects user to Home page | Pass |
| Sign out page | Click on Sign out | Redirects user to Home page / Success Toast | Pass |

### Products
| Feature | Test | Expected Result | Result |
| -------------| ----- | ----- | :----: |
| Product Detail | Click on a product | Redirect to product's details | Pass |
| Add to Wishlist | Click on Add To Wishlist icon | Icon lights / Item moves to users wishlist | Pass |
| Category | Click on Category (League) | Redirects to Category | Pass |
| Ratings | Click on Ratings | Dropdown menu to rate the product | Pass |
| Rate | Select a rating and Submit | Add rating to ratings / Sucess Toast | Pass |
| Update Rating | Select a new rating and Submit | Rating changed / Success Toast _Rating Updated_ | Pass |
| Size | Click on size's dropdown menu | Select a size | Pass |
| Quantity | Click on (+ or -) buttons | Select a quantity (max of 5 units per product) | Pass |
| Add to Cart | Clic on Add to Cart button | Item moves to Cart / Success Toast / Pass |
| Products | Click on Products button | Redirect to All Products page | Pass |

### Shopping Cart
| Feature | Test | Expected Result | Result |
| -------------| ----- | ----- | :----: |
| Shopping Cart List | List of products added | Show product selected sizes, quantities, prices and subtotal |
| Edit Quantity | Click on (+ or -) buttons and Update | Recalculate all amounts in Cart / Success Toast | Pass |
| Delete Product | Click on Remove | Remove product from Cart / Success Toast | Pass |
| Shopping Cart Total | Shows amount without discount | Shows amount without discount | Pass |
| Discount Applied | Shows amount discounted (if applyed) | Shows amount discounted (if applyed) | Pass |
| Discount Applied | Shows no field (if no applyed) | Shows no field (if no applyed) | Pass |
| Shipping | Shows Shipping costs (if applyed) | Shows Shipping costs (if applyed) | Pass |
| Grand Total | Shows the final amount to pay by user | Shows the final amount to pay by user | Pass |
| *Recalculate Amount Fields | Update quantity or remove items | Shows recalculated amounts | Pass |
| Back to Shop | Click Back to Shop button | Redirects to All Products | Pass |
| Secure Check out | Click on Secure Check out | Redirects to Purchase Page | Pass |

### Purchase
| Feature | Test  | Expected Result | Result |
| -------------| ----- | ----- | :----: |
| Checkout View | Shows Purchase form and Resume of products | Shows Purchase form and Resume of products | Pass |
| Products' Resume | Shows Item, size, quantity | Shows Item, size, quantity | Pass |
| Amount Resume | Shows Subtotal, Total, Discount, Shipping Costs and Grand Total | Shows Subtotal, Total, Discount, Shipping Costs and Grand Total | Pass |
| Purchase Form | Fill form with correct data and Submit | Redirects to Purchase Success / Email confirmation sent / Success Toast / | Pass |
| Purchase Form | Fill form with blank fields | Alerts user about it | Pass |
| Purchase Form | Fill form with blank card details | Atempts to process, fail and alerts user about it | Pass |
| Purchase Form | Fill form with invalid card details | Atempts to process, fail and alerts user about it | Pass |
| Update Cart | Click Update Cart button | Redirects to Shopping Cart | Pass |

### ADMIN:

### Add Product:
| Feature | Test  | Expected Result | Result |
| -------------| ----- | ----- | :----: |
| Add New Product | Click on Management in User's Account Icon | Redirect to Add New Product Page | Pass |
| Product Management | Add New Product form | Shows the form for adding new product | Pass |
| Add New Product form | Fill the form with correct data | Creates new product in the shop / Success Toast | Pass |
| Add New Product form | Fill the form with blank data | Alerts the admin about it | Pass |
| Add New Product form | Fill the form with no picture | Creates new product in the shop without picture / Success Toast | Pass |

### Edit Product:
| Feature | Test  | Expected Result | Result |
| -------------| ----- | ----- | :----: |
| Edit Product | Click on Edit in the Product Detail | Updates product / Redirect to Edit Product Page / Info Toast | Pass |
| Edit Product | Edit product fields and click on Update Product | Redirect to Product Detail Page / Success Toast | Pass |
| Edit Product | Leave blank fields and click on Update Product | Alerts the admin about it | Pass |

### Delete Product:
| Feature | Test  | Expected Result | Result |
| -------------| ----- | ----- | :----: |
| Delete Product | Click on Delete in the Product Detail | Delete product / Redirect to All Products / Success Toast |



