require 'lib/carm'

set :site_title, "Move Fast and Make Things in Python"
set :site_deck, "Python practical tutorials and recipes"
set :site_description, "A brief practical guide to Python aimed at data and computational journalism"


activate :directory_indexes
activate :i18n, :mount_at_root => :en
activate :livereload
activate :syntax, :line_numbers => false

############################ assets
set :markdown_engine, :kramdown
set :slim, :pretty => true
set :trailing_slash, true
set :css_dir, 'assets/stylesheets'
set :js_dir, 'assets/javascripts'
set :images_dir, 'assets/images'

############################# layout stuff
set :layout, 'page'
page "/recipes/*", :layout => "recipe"
page "/chapters/*", :layout => "chapter"

############################# Build-specific configuration
configure :build do

end
