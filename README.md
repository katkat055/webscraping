## Internet Development II (ITAS256)

## Assignment 1 – Web Scraping

Date assigned: February 5, 2024

Date due: **February 16, 2024**

**Learning Objectives**

Upon successful completion of this assignment, the student will be able to:

- Use Python libraries to access websites.
- Use Python web scraping techniques to scrape web pages.
- Assemble data scraped from websites.
- Convert list data to json.
- Write data to files.

**To be uploaded to the Github:**

This assignment will be submitted through Github. I have created the main branch here. You must create your own branch called *\<\<yourusername\>\>*-256A01, where *\<\<yourusername\>\>* is substituted with your actual username. When you have completed the assignment, add a single line comment to the assignment on the portal so I know that you are done. Also, add a tag to your code branch with the name '*\<\<yourusername\>\>*-complete'.

**To Start:**

1. Create a branch from this repository at \<\<url\>\> with the format above. Make sure that the branch is private so that only you (and I as repo owner) can see it.
2. Clone the repo to your local machine to work on it. I suggest keeping your code synced regularly. That will also be easier if you have any questions.
3. You can do this assignment with the standard python library if you wish. You may also (and I recommend doing so) use the requests library and the Beautiful Soup library for making the requests and extracting the information. Please use Beautiful Soup 4 if you use it.

**To Do:**

1. You are going to scrape the information off two websites to see if there are jobs that you want to apply for. The first is [www.viatec.ca](http://www.viatec.ca/). This is a site that posts for resources for tech jobs in the Victoria area. The second site will be [https://ca.indeed.com/?r=ca](https://ca.indeed.com/?r=ca) which is a large database of jobs from around the world.
2. Indeed: go to the indeed website and enter 'developer' for the Job title and Vancouver Island for the location. Select Find Jobs and look at the URL. It should be something like: [https://ca.indeed.com/jobs?q=developer&l=Vancouver+Island&vjk=93f76e3c52844c62](https://ca.indeed.com/jobs?q=developer&l=Vancouver+Island&vjk=93f76e3c52844c62). Note, in particular, the query string. The q is the job title, and the L is the location. The vjk parameter is irrelevant for our purposes. So, the URL can be: [https://ca.indeed.com/jobs?q=developer&l=Vancouver+Island](https://ca.indeed.com/jobs?q=developer&l=Vancouver+Island).
3. Look at the source code for the web page (Ctrl-U on most browsers). Each individual job is buried inside a div with the class cardOutline (there will likely be other classes too so you cannot just look for the attribute with that class name).
4. Inside this div is an h2 tag (with the class jobTitle) with an \<a\> tag and inside the \<a\> tag a \<span\> tag. The data from that span tag is the job title.
5. Farther down is a \<span\> tag with the attribute data-testid="company-name". The data from that tag contains the company name.
6. Farther down is a \<div\> with the attribute data-testid="text-location". The data from the tag contains the location.
7. Use a request object to scrape the information from the page using the URL with the query string appended to it. As above, you can use the standard Python library or something like the requests library.
8. Parse the page returned (HTML Parser or Beautiful Soup) and create a list (or similar) of the three pieces of data above.
9. Save each of these pieces of data in a list. In the end you should have the Job title, Company name and location. Write this information as a JSON file called joblist.json with each record looking as below:

![output file](https://github.com/ITAS-Git/ITAS256-A01/blob/main/images/img1.png)

1. Optionally, you can loop with multiple job titles such "developer", "programmer" and "full-stack". Append the data each time and try to eliminate duplicates.
2. Viatech: go to the Viatec site and look at the job board. Under the Categories drop down select Software and Programming Jobs and press Search. Check out the URL it should look something like: [https://members.viatec.ca/job-board/Search?term=&DateFilter=0&from=&to=&CategoryValues=235246](https://members.viatec.ca/job-board/Search?term=&DateFilter=0&from=&to=&CategoryValues=235246). Note, in particular, the query string. The term, DateFilter, from and to options are empty; the only one actually used is the CategoryValues. So the URL can be reduced to: [https://members.viatec.ca/job-board/Search?CategoryValues=235246](https://members.viatec.ca/job-board/Search?CategoryValues=235246).

Note: If you want to see other categories you can select them from the drop down menu. Only the CategoryValues value will change on the URL.

1. Look at the source code for the web page (Ctrl-U on most browsers). Each individual job is inside a div with the class(es) card-body and gz-content-body. Inside this div is another div and inside that is an \<a\> tag. The data (between the start and end tag) for this tag is the job title. The href attribute of this tag provides the details about the job. You need to extract/save both of these pieces of information.
2. There is a second \<a\> tag. The href of the second \<a\> tag is the link to the page about the company posting the job. You will need that information too. (see image)

![viatec site](https://github.com/ITAS-Git/ITAS256-A01/blob/main/images/img2.png)

1. Use a request object to scrape the information from the page using the URL above. As above, you can use the standard Python library or something like the requests library.
2. Parse the page returned (HTML Parser or Beautiful Soup) and create a list (or similar) of the three pieces of data above.
3. Now loop through the list and, using the second href (the one to the page about the company) retrieve that page.
  1. Use a requests to scrape the information from the page. The company name is data from the the \<h1\> tag with the class gz-pagetitle.
  2. Also scrape the primary contact information. This can be found inside a div with the class row gz-details-reps. Inside that div you are looking for the div immediately following the div with the class gz-prim-contact and getting the data from the divs with the classes gz-member-repname and gz-member-reptitle (See image)

  ![viatec site](https://github.com/ITAS-Git/ITAS256-A01/blob/main/images/img3.png)

1. For each job, get the data that indicates the contacts name and title. Unfortunately, there is no easy way to get an email address as that is kept in the membership directory.
2. So, in the end you should have the Job title, Details link, Company name, primary contact name and title. Append this information to the JSON file called joblist.json. (You do not care about second URL anymore) Now the list looks like:

![output file](https://github.com/ITAS-Git/ITAS256-A01/blob/main/images/img4.png)

Note: If a piece of data is missing simply make it an empty string. Also, make sure that the output file is formatted properly when you write it (the json.dumps method does that).

**Assignment Marking Scheme**

The following marking scheme will be used in marking the assignment.

|Criteria| Out of |
|--------| ------ |
| **Scraped indeed.com and extracted jobs** | 20 |
| **Gathered proper information on indeed jobs** | 10 |
| **Extracted information and stored in JSON file** | 10 |
| **Scraped viatec.com and extracted jobs** | 15 |
| **Gathered proper information on viatec jobs** | 10 |
| **Got further information on viatec johbs such as company and contact** | 15 |
| **Extracted information and appended to JSON file** | 5 |
| **Coding Style<br>- PEP 8 followed<br>- Good use of functions** | 10 |
| **Organization**<br>- assignment folder and project named according to standards<br>- assignment added to Github repository properly** | 5 |
| **Total** | 100 |
