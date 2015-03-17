require 'lib/content_article'
class ContentCollection
  # expects arr to be a bunch of resources
  attr_reader :slug, :title
  def initialize(the_slug, arr)
    @slug = the_slug
    @title = @slug
    @items = arr
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
    articles[idx - 1]
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


def ContentCollection(the_slug, arr)
  ContentCollection.new(the_slug, arr)
end
