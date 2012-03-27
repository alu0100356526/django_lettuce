<!DOCTYPE html>
<html>
  <head>
    <title>{% block title %} Sample App {% endblock %}</title>
    <!--[if lt IE 9]>
    <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
    <link rel="stylesheet" type="text/css" href="{{ STATIC_URL }}screen.css">
    <link rel="stylesheet" type="text/css" href="{{ STATIC_URL }}print.css">
    <!--[if lt IE 8]><link rel="stylesheet" type="text/css" href="{{ STATIC_URL }}ie.css"><![endif]-->
    <link rel="stylesheet" type="text/css" href="{{ STATIC_URL }}custom.css">
  </head>
  <body>
    <div class="container">
      <header>
		  <img class="round" src="{{ STATIC_URL }}logo.png" alt="Sample App">
        <nav class="round">
          <ul>
				{% url staticpages.sample_app.views.home as hm %}
				{% url staticpages.sample_app.views.help as hlp %}
				<li><a href="{{ hm }}">Home</a></li>
				<li><a href="{{ hlp }}">Help</a></li>
				<li><a href="#">Sign in</a></li>  <!-- Por ahora Sign in no va a ningún lado. -->
          </ul>
        </nav>
      </header>
      <section class="round">
        {% block content %}{% endblock %}
      </section>
      <footer>
			<nav class="round">
				<ul>
					{% url staticpages.sample_app.views.about as ab %}
					{% url staticpages.sample_app.views.contact as ct %}
					<li><a href="{{ ab }}">About</a></li>
					<li><a href="{{ ct }}">Contact</a></li>
				</ul>
			</nav>
		</footer>
    </div>
  </body>
</html>
