
# ABCs Are Mixins Too
# first example comes from python's abc package
# collections.abc uses mixins to provide functionalities

# ThreadingMixIn and ForkingMixIn
# The http.server package provides HTTPServer and 
# ThreadingHTTPServer classes. The latter was added in Python 3.7. Its documentation says:
## class http.server.ThreadingHTTPServer(server_address, RequestHandlerClass)
### This class is identical to HTTPServer but uses threads to handle requests by using the ThreadingMixIn.
### This is useful to handle web browsers pre-opening sockets, on which HTTPServer would wait indefinitely.


# Django Generic Views Mixins
