def carm
  Carm.new(sitemap)
end


def current_content_resource
  carm.get_content_resource(current_page)
end


def get_content_resource(val)
  carm.get_content_resource(val)
end


def link_to_content_resource(val)
  c = get_content_resource(val)

  link_to c.title, c.url
end

########
def carm_chapters
  carm.chapters
end

def carm_categorized_recipes
  carm.categorized_recipes
end

# returns:
#   A ContentResource (Chapter) that comes after the given
#   order_val
#
# params:
#   val:
#      if nil: uses current_content_resource()
def carm_next_chapter(val = nil)
  r = val.nil? ? current_content_resource : val

  carm.next_chapter(r)
end

def carm_prev_chapter(val = nil)
  r = val.nil? ? current_content_resource : val

  carm.prev_chapter(r)
end


