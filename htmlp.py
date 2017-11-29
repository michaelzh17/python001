# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

#parser = MyHTMLParser()
#parser.feed('''''')


parser01 = MyHTMLParser()
parser01.feed('''                            
<time datetime="2017-11-29T00:00:00+00:00">29 Nov. &ndash; 01 Dec. <span class="say-no-more"> 2017</span></time>

                            

                            
                            <span class="event-location">LCH, IIT Bombay, Powai, Mumbai, India</span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/552/">Kiwi PyCon 2017</a></h3>
                        <p>
                            
                            
<time datetime="2017-12-02T00:00:00+00:00">02 Dec. &ndash; 04 Dec. <span class="say-no-more"> 2017</span></time>

                            

                            
                            <span class="event-location">Auckland, New Zealand</span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/556/">North Bay Python 2017</a></h3>
                        <p>
                            
                            
<time datetime="2017-12-02T00:00:00+00:00">02 Dec. &ndash; 04 Dec. <span class="say-no-more"> 2017</span></time>

                            

                            
                            <span class="event-location">Petaluma, California, USA</span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/612/">PyCon Indonesia 2017</a></h3>
                        <p>
                            
                            
<time datetime="2017-12-09T00:00:00+00:00">09 Dec. &ndash; 10 Dec. <span class="say-no-more"> 2017</span></time>

                            

                            
                            <span class="event-location">Surabaya, Indonesia</span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/563/">PyCon Pakistan</a></h3>
                        <p>
                            
                            
<time datetime="2017-12-16T00:00:00+00:00">16 Dec. &ndash; 17 Dec. <span class="say-no-more"> 2017</span></time>

                            

                            
                            <span class="event-location">Lahore, Pakistan</span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/543/">PyCascades 2018</a></h3>
                        <p>
                            
                            
<time datetime="2018-01-22T00:00:00+00:00">22 Jan. &ndash; 24 Jan. <span class="say-no-more"> 2018</span></time>

                            

                            
                            <span class="event-location">Vancouver, BC V6A, Canada</span>
                            
                        </p>
                    </li>
                
                </ul>
            </div>

            
            <h3 class="widget-title just-missed">You just missed...</h3>
            <ul class="list-recent-events menu">
                
                <li>
                    <h3 class="event-title"><a href="/events/python-events/598/">PyTexas 2017</a></h3>
                    <p>
                        
                        
<time datetime="2017-11-18T00:00:00+00:00">18 Nov. &ndash; 19 Nov. <span class="say-no-more"> 2017</span></time>

                        
                        
                        
                        <span class="event-location">119 Nueces St, Austin, TX 78701, USA</span>
                        
                    </p>
                </li>
                
                <li>
                    <h3 class="event-title"><a href="/events/python-events/609/">PyCon Canada 2017</a></h3>
                    <p>
                        
                        
<time datetime="2017-11-18T00:00:00+00:00">18 Nov. &ndash; 22 Nov. <span class="say-no-more"> 2017</span></time>

                        
                        
                        
                        <span class="event-location">Montreal, Quebec, Canada</span>
                        
                    </p>
                </li>
                
            </ul>
            
        </div>
''')



