def carm
  Carm.new(sitemap)
end


def current_content_article
  carm.get_content_article(current_page)
end


def get_content_article(val)
  carm.get_content_article(val)
end


def link_to_contents
  link_to "Contents", "/contents/"
end

def link_to_content_article(val)
  if val.is_a?(Hash)   # i.e. just a slug
    c = get_content_article(val[:slug])
    t = val[:title] || c.title
    n = val[:notes] || nil

  else
    c = get_content_article(val)
    t = c.title
    n = nil
  end

  if n.present?
    [link_to(t, c.url), n].join(' - ')
  else
    link_to t, c.url
  end
end

def link_to_article_collection(val)
  c = get_content_article(val)
  link_to 'TK', '/'
#  link_to c.collection_title, c.collection_url
end

########
def carm_lessons
  carm.lessons
end

def carm_recipes
  carm.recipes
end

# returns:
#   A ContentArticle (Chapter) that comes after the given
#   order_val
#
# params:
#   val:
#      if nil: uses current_content_article()
def carm_next_article(val = nil)
  r = val.nil? ? current_content_article : val

  carm.next_article(r)
end

def carm_prev_article(val = nil)
  r = val.nil? ? current_content_article : val

  carm.prev_article(r)
end


