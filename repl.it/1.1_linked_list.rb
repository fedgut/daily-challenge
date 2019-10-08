class Node
  attr_accessor :value, :next_node
  
  def initialize(value, next_node = nil)
	  @value = value
    @next_node = next_node
  end
end

class LinkedList
  @head = nil
  @tail = nil
  attr_accessor :head, :tail

  def add(number)
    new_node = Node.new(number)
    if !@head
      @head = new_node
    end
    if !@tail
      @tail = new_node
    else 
      @tail.next_node = new_node 
    end
  end

  def get(index)
    current = @head
    count = 0
    while (current) do
      if (count == index)
        return current.value
      end
      count += 1
      current = current.next_node
    end
  end
end

list = LinkedList.new

list.add(3)
list.add(5)
puts list.get(1)

