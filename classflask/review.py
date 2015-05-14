import re


class MyApp:

    def __call__(self, environ, start_response):


        path = str(environ['PATH_INFO'])

        output = ""
        

        

        changer = re.findall("[aeiouAEIOU]+", path)
        matchObj = re.match("(luther)(.+)([0-9]+)(college)(.+)", path)
        

       # if len(changer)==(len(path)-1):
        if changer:
            worker = ""
            changeLen = len(changer)
            for i in range(changeLen):

                worker+=changer[i]


            output = "All the vowels are " + worker + "!"
            data = bytes(output, 'utf-8')

            start_response("200 OK", [
                    ("Content-Type", "text/plain"),
                    ("Content-Length", str(len(data)))])

            return [data]

        elif matchObj:

            #####Save number before college

            savedDate = matchObj.group(3)

            output = "Did you graduate in " + savedDate + "?"

            data = bytes(output, 'utf-8')

            start_response("200 OK", [
                    ("Content-Type", "text/plain"),
                    ("Content-Length", str(len(data)))])
            

            return [data]

        else:

            start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])

            return "404 Not Found"

        
        





matchapp = MyApp()
