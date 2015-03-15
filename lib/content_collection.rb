require 'lib/content_resource'
class ContentCollection
  # expects arr to be a bunch of resources
  def initialize(arr)
    @items = arr.map{ |a| ContentResource(a) }.sort_by{|a| a.ordernum.to_i }
  end


  def next_resource(r)
    idx = get_index_of_content(r)
    @items[idx + 1]
  end

  def prev_resource(r)
    idx = get_index_of_content(r)
    @items[idx - 1]
  end

  ### make it enumerable
  def each
    return enum_for(:each) unless block_given?
    @items.each do |i|
      yield i
    end
  end

  def find(*args, &blk)
    @items.find(*args, &blk)
  end
  def index(*args, &blk)
    @items.index(*args, &blk)
  end

  def [](*args)
    @items[*args]
  end

  private
    def get_index_of_content(r)
      idx = self.index{|c| c.slug == r.slug }
    end
end


def ContentCollection(arr_resources, *terms)
  arrterms = Array(terms)
  regexterms = arrterms.map{|t| Regexp.escape(t) }.join('|')
  arr = arr_resources.select{ |r| r.path =~ /(?:#{regexterms})\// }

  ContentCollection.new(arr)
end
