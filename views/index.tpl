<!DOCTYPE html>
<html>
  <head>
  <charset="utf-8">
  <link rel="stylesheet" href="/css/pure-min.css">
  <link rel="stylesheet" href="/css/main.css">
  <title>eng2jpn_srv</title>
  </head>

  <body>
  <div class="header">
  <div class="home-menu pure-menu pure-menu-horizontal pure-menu-fixed">
        <a class="pure-menu-heading" href="/">eng2jpn_srv</a>
  </div></div>
  <br><br>

  <h3 class="content-subhead"> English </h3>
  <form action="/" method=post>
  <textarea class="eng_form" name="eng_txt" rows="10" cols="100">
% if eng_txt is not None:
{{eng_txt}}
% end
</textarea>
  <button class="button-success pure-button" type="submit">translate!</button>
</form>

  <h3 class="content-subhead"> Japanese </h3>
  <textarea class="jpn_form" name="jpn_txt" rows="15" cols="100">
% if jpn_txt is not None:
{{jpn_txt}}
% end
</textarea>
<button class="button-error pure-button" type="button" onClick="location.href='/'">clear</button>

  </body>
</html>
