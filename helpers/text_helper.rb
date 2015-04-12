
def make_markdown(str)
  Kramdown::Document.new(str.to_s).to_html
end


def brief_codepiece(fpath, opts = {})
  xopts = opts.merge({:display_class => 'brief'})

  codepiece(fpath, xopts)
end

def codepiece(fpath, opts = {})
  fname = File.join("/code/", fpath)
  raw_content = get_raw_content_from_file(fname)
  splits = raw_content.split(/^# ----$/)
  if splits.count > 1
    polished_content = splits[1..-1].join("\n# ----\n").strip
  else
    polished_content = raw_content
  end

  # determine language
  lang = opts[:lang] || case File.extname(fpath)
  when /rb/   ; 'ruby'
  when /py$/  ; 'python'
  when /sh$/  ; 'shell'
  when /html/ ; 'html'
  when /xml/  ;  'xml'
  when /css/  ;  'css'
  when /json/ ;  'json'
  when /yaml/ ;  'yaml'
  else
    nil
  end

  display_class = opts[:display_class]

  partial "/layouts/partials/codepiece",
    locals: { content: polished_content, display_class: display_class,
              lang: lang, path: fname, url: fname, }

#  partial "/layouts/partials/code_snippet",
#    locals: { content: polished_content, path: resource.path, url: resource.url }
end


# hacky!
# was having trouble with getting files in /code
def get_raw_content_from_file(path)
  if contains_leading_underscore?(path)
    # attempt absolute path
    z = File.expand_path(path, sitemap.app.source_dir)
    File.read(z)
  else
    sitemap.find_resource_by_path(path).render
  end
end


def contains_leading_underscore?(path)
  path.to_s.split('/').any?{|p| p =~ /^_/ }
end


def link_to_reference(obj)
  u = URI.parse(obj['url'])
  title = obj['title'] || truncate(u.to_s, length: 125)

  link_to title, u.to_s
end
