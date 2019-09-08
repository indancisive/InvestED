# InvestED
## Inspiration:

Investing can be a daunting task for those who are unfamiliar with technical analysis and financial jargon. With a strong focus on accessibility and minimalism, InvestED was created first and foremost with the aspiration of improving the financial literacy of younger generations.

We hope that InvestED will act not only as a stepping stone into the often intimidating world of investing, but also as an educational tool that presents accurate market outlooks using bleeding edge data from Goldman Sachs' Marquee.

## What it does:

InvestED guides users through a step-by-step process that explains their choices when analyzing what to invest in in a simplified and easy-to-understand manner. InvestED streamlines the investing experience for those new to the field and makes it accessible through its beautiful UI.

## How we built it:

We built a Python-based webapp using Django as the web framework and UIKit as the frontend CSS framework. 
Using the `marquee_data_interface.py` script we wrote (packaged with InvestED), we queried Goldman Sachs' 
USCANFPP dataset sourced from the Marquee API and indexed it in an SQL database. Then, we analyzed the various contextual investment factors from the database and used them to calculate the ideal stock for users to invest in, considering their input.

## Challenges we ran into:

As a group of relatively new hackers, our inexperience often lended itself to slowing down our full stack solution. For example, we had to learn how to utilize SQL databases (not to mention in conjunction with Django) with no prior experience in order to speed up our load times, as well as struggle through the API documentation of Marquee which while feature-rich, frequently left us puzzled.

## Accomplishments we are proud of:

While on one end standing as challenges, conquering these obstacles left us with an unparalleled sense of pride. Spending several hours fiddling with the Marquee API's data through our script only for it finally appear in our SQL3db browser line by line might not be immensely impressive, but we learned tremendously from it.


## What we built it with:

Goldman Sachs Marquee API - Used to retrieve raw investment and financial indicators and information on stocks

UIKit - Front-end Web CSS framework

Django/Python - Back-end Web Framework

SQLite - Database

JavaScript - Animations
