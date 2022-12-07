class Tree:
    @@name
    @@parent
    @@children = {}
    @@files = {}
    
    def initialize(name, parent=nil)
        @@name = name
        @@parent = parent
    end

    def mkdir(name)
        @@children[name] = new Tree(name, self)
        return @@children[name]
    end

    def touch(size, name)
        files[name] = size.to_i
    end

    def root
        nil
    end

    def size
        nil
    end
end