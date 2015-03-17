require 'lib/carm'
Slim::Engine.disable_option_validator!

set :mfamt_topic, 'Python'
set :mfamt_title, "Move Fast and Make Things in #{mfamt_topic}"
set :site_title, config[:mfamt_title]

set :site_deck, "Python practical tutorials and recipes"
set :site_description, "A practical guide to Python aimed at data and computational journalism"


activate :directory_indexes
activate :i18n, :mount_at_root => :en
activate :livereload
activate :syntax, :line_numbers => false

######### assets
set :markdown_engine, :kramdown
set :slim, :pretty => true

set :trailing_slash, true
set :css_dir, 'assets/stylesheets'
set :js_dir, 'assets/javascripts'
set :images_dir, 'assets/images'

######### layout stuff
set :layout, 'page'
page "/content/*", :layout => "content"

############################# Build-specific configuration
configure :build do

end




activate :s3_sync do |s3_sync|
  s3_sync.bucket                     = 'python.mfamt.org' # The name of the S3 bucket you are targetting. This is globally unique.
  s3_sync.region                     = 'us-east-1'     # The AWS region for your bucket.
  s3_sync.delete                     = false # We delete stray files by default.
  s3_sync.after_build                = true # We do not chain after the build step by default.
  s3_sync.prefer_gzip                = false
  s3_sync.path_style                 = true
  s3_sync.reduced_redundancy_storage = false
  s3_sync.acl                        = 'public-read'
  s3_sync.encryption                 = false
  s3_sync.prefix                     = ''
end

