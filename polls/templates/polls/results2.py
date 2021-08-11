<h1>{{ question.question_text }}</h1>

<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
{% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">Vote again?</a>

<article>
    <h1>This is a headline.</h1>
    <p>This is my first paragraph.</p>
    <p>This is the second paragrah.</p>
    <p>This third paragraph has <em>text that's emphasized</em> for effect.</p>
</article>
