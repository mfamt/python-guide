require 'lib/content_resource'
require 'lib/content_collection'

class Carm
  RECIPE_CATS = %w(informal practical project)
  def initialize(sitemap)
    @site_resources = sitemap.resources
  end

  def chapters
    resources('chapters')
  end

  def categorized_recipes
    RECIPE_CATS.inject({}) do |h, k|
      h[k] = self.send("#{k}_recipes".to_sym)

      h
    end
  end

  RECIPE_CATS.each do |r|
    define_method "#{r}_recipes" do
      resources(r)
    end
  end

  def resources(scope = nil)
    if scope.present?
      ContentCollection(@site_resources, scope)
    else
      ContentCollection(@site_resources, 'chapters', 'recipes')
    end
  end


  def next_resource(val)
    r = get_content_resource(val)
    coll = get_content_collection_for_resource(r)
    coll.next_resource(r)
  end

  def prev_resource(val)
    r = get_content_resource(val)
    coll = get_content_collection_for_resource(r)
    coll.prev_resource(r)
  end

  def next_chapter(val)
    next_resource(val)
  end

  def prev_chapter(val)
    prev_resource(val)
  end

  def get_content_resource(val, scope = nil)
    case val
    when ContentResource
      val
    when Middleman::Sitemap::Resource
      ContentResource(val)
    else
      # assume it's a string path or ordernum
      if val =~ /\/\w+/ # it's a path
        get_content_resource_by_path(val)
      else
        get_content_resource_by_ordernum(val, scope)
      end
    end
  end


  def self.slugify(path)
    ContentResource.slugify(path)
  end

  private
    # assuming :chapters is an Array
    # returns index of chapter in Array


    def get_content_collection_for_resource(val)
      r = get_content_resource(val)
      resources(r.scope)
    end

    def get_content_resource_by_ordernum(num, scope = nil)
      onum = num.to_i

      if scope.present?
        resources(scope).find{|c| c.ordernum == onum }
      else
        resources.find{|c| c.ordernum == onum }
      end
    end

    def get_content_resource_by_path(path)
      pslug = Carm.slugify(path)

      chapters.find{|c| c.slug == pslug }
    end
end
