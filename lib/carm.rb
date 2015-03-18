require 'lib/content_article'
require 'lib/content_collection'
require 'lib/content_scope'

class Carm
  attr_reader :content_articles
  def initialize(sitemap)
    @sitemap = sitemap
    @site_resources = sitemap.resources
    @content_articles = formulate_content_articles
  end


  def lessons
    scopes['lessons']
  end

  def recipes
    scopes['recipes']
  end


  def scopes
    metacontent.each_pair.inject({}) do |hsh, (scope_slug, scope_obj)|
      scope_articles = @content_articles.select{|r| r.url =~ /\/content\/#{Regexp.escape(scope_slug)}\// }
      hsh[scope_slug] = ContentScope(scope_slug, scope_obj, scope_articles)

      hsh
    end
  end


  def next_article(val)
    r = get_content_article(val)
    coll = get_content_collection_for_article(r)
    coll.next_article(r)
  end

  def prev_article(val)
    r = get_content_article(val)
    coll = get_content_collection_for_article(r)
    coll.prev_article(r)
  end

  def get_content_article(val)
    case val
    when ContentArticle
      val
    when Middleman::Sitemap::Resource
      ContentArticle(val)
    else
      # assume it's a string path
      if val =~ /\/\w+/ # it's a path
        get_content_article_by_path(val)
      else
        raise StandardError, '#get_content_article() needs a useful identifier'
      end
    end
  end


  def self.slugify(path)
    ContentArticle.slugify(path)
  end

  private
    # assume that data.metacontent holds the data
    def metacontent
      @sitemap.app.data.metacontent
    end

    # assuming :lessons is an Array
    # returns index of chapter in Array
    def formulate_content_articles
      @site_resources.select{|r| r.url =~ /\/content\// }.
        reject{|c| c.path =~ /index.html/ }.
        map{|c| ContentArticle(c) }.
        sort_by{ |a| a.ordernum.to_i }
    end

    def get_content_collection_for_article(val)
      r = get_content_article(val)
      s = get_content_scope_for_article(r)

      s.get_collection_for_article(r)
    end

    def get_content_scope_for_article(val)
      r = get_content_article(val)

      self.scopes.find{|c| c.slug == r.scope_slug}
    end

    def get_content_article_by_path(path)
      pslug = ContentArticle.slugify(path)

      lessons.find{|c| c.slug == pslug }
    end
end
