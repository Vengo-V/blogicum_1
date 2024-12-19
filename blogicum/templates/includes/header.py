{% load static %}

<header>
  <nav class="navbar navbar-light" style="background-color: lightskyblue">
    <div class="container">
      <a class="navbar-brand" href="{% url 'blog:index' %}">
        <img src="{% static 'img/logo.png' %}" width="30" height="30" class="d-inline-block align-top" alt="">
        Блогикум
      </a>        
      <ul class="nav  nav-pills">
        <li class="nav-item">
          <a class="nav-link active" href="{% url 'blog:index' %}">
            Лента записей
          </a>
        </li>
        <li class="nav-item">              
          <a class="nav-link" href="{% url 'pages:about' %}">
            О проекте
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'pages:rules' %}">
            Наши правила
          </a>
        </li>
      </ul>      
    </div>
  </nav> 
</header>
