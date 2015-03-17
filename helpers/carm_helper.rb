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
  c = get_content_article(val)

  link_to c.title, c.url
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


