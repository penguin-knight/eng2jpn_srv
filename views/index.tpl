<!DOCTYPE html>
<html>
  <head>
  <charset="utf-8">
  <link rel="stylesheet" href="/static/css/pure-min.css">
  <link rel="stylesheet" href="/static/css/main.css">
  <title>eng2jpn_srv</title>
  </head>

  <body>
  <div class="header">
  <div class="home-menu pure-menu pure-menu-horizontal pure-menu-fixed">
        <a class="pure-menu-heading" href="/">eng2jpn_srv</a>
  </div></div>
  <br><br>

  <h3 class="content-subhead"> English </h3>
  <form name="txt" action="/" method=post>
  <textarea class="eng_form" name="eng_txt" rows="10" cols="100">
% if eng_txt is not None:
{{eng_txt}}
% end
</textarea>

  <h3 class="content-subhead"> Japanese </h3>
  <textarea class="jpn_form" name="jpn_txt" rows="15" cols="100">
% if jpn_txt is not None:
{{jpn_txt}}
% end
</textarea>
<p>
<button class="button-success pure-button" type="submit">translate!</button>
<button class="button-error pure-button" type="button" onClick="reset_form()">clear</button>
</p>

<a class="button-warning pure-button" href="/format_eng">format text</a>

</form>
<script type="text/javascript" src="/static/js/main.js"></script>
  </body>
</html>
