  <div class="grid-container">
  <h1>Media Items<h1>
    <div class="grid-margin-x grid-x">
    {% for media in media_items %}
      <div class="small-3 cell">
      <a href="{{  'media/'+ media.id | string }}">
        <p>{{ media.title }}</p>
        <div class='image'>
          <img src="{{ media.thumbnail_url }}" />
        </div>
      </a>
      </div>
    {% endfor %}
    <div>
  </div>
