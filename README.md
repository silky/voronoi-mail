Voronoi-mail
===========

Installation
--

 1) pip install [any dependency]
  
    specifically: pip install xmltodict


Running
--

 1) Open up the folder, write "python -m CGIHTTPServer 8000", which will start the webserver on port 8000.
  
 2) Browse to http://localhost:8000/ and type in gmail account details
 

Trivia
--

 * The POST request to pass the credentials from the page to itself isn't over SSL. This may or may not
	be an issue (note that the server is only running via localhost; don't run this publically!)
 
 * If you append "?unique", the emails with the same email accounts will be (probably) coloured uniquely,
	otherwise they will be coloured the same (though other emails may clash in the colouring.)
  
 * The Gmail API appears to only want to ever return 20 new emails.
  
