require 'lib/content_article'
class ContentCollection
  # expects arr to be a bunch of resources
  attr_reader :slug, :title, :description
  def initialize(the_slug, obj, col_articles)
    @slug = the_slug
    @title = obj.title
    @description = obj.description
    @items = col_articles
  end

  def articles
    @items
  end

  def next_article(r)
    idx = get_index_of_content(r)
    articles[idx + 1]
  end

  def prev_article(r)
    idx = get_index_of_content(r)
    idx > 0 ? articles[idx - 1] : nil
  end

  ### make it enumerable
  def each
    return enum_for(:each) unless block_given?
    articles.each do |i|
      yield i
    end
  end

  def find(*args, &blk)
    articles.find(*args, &blk)
  end
  def index(*args, &blk)
    articles.index(*args, &blk)
  end

  def [](*args)
    articles[*args]
  end

  private
    def get_index_of_content(r)
      idx = self.index{|c| c.slug == r.slug }
    end
end


def ContentCollection(the_slug, obj, arr)
  ContentCollection.new(the_slug, obj, arr)
end
