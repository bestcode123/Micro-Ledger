for i4 in range(5):
    for i3 in range(128):
        for i2 in range(32):    
            import keygen

            level = 2
            bit_size = 32
            end = ''

            for i in range(bit_size):
                end += keygen.Keygen('alphabet').gen_key(bit_size)

            def tobin(val):
                end = ''
                for i in range(len(str(bin(val)))):
                    if(i == 0):
                        pass
                    elif(i == 1):
                        end += '0'
                    else:
                        end += str(bin(val))[i]
                return end


            def xor(bin1, bin2):  # Required to be of the same size
                end = ''
                for i in range(len(bin1)):
                    if(bin1[i] == '0' and bin2[i] == '0'):
                        end += '0'
                    elif(bin1[i] == '1' and bin2[i] == '0'):
                        end += '1'
                    elif(bin1[i] == '0' and bin2[i] == '1'):
                        end += '1'
                    elif(bin1[i] == '1' and bin2[i] == '1'):
                        end += '0'
                return end

            alphabet = [['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','o','q','r','s','t','u','v','w','x','y','z'],
                        [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]]

            end1 = ''
            end2 = ''

            endmax = len(end)

            for i in range(endmax):
                if(i < endmax / 2):
                    end1 += end[i]
                else:
                    end2 += end[i]

            ends = [end1, end2]
            ends2 = []

            for i in range(len(ends)):
                endx = []
                for j in range(len(ends[i])):
                    endx.append(str(alphabet[1][alphabet[0].index(ends[i][j])]))
                ends2.append(endx)

            ends3 = []

            for i in range(len(ends2)):
                endx2 = []
                for j in range(len(ends2[i])):
                    endx2.append(tobin(int(ends2[i][j])))
                ends3.append(endx2)


            endend = ''

            for i in range(len(ends3[0])):
                endend += xor(ends3[0][i], ends3[1][i])

            with open('ledger/' + str(i4) + '/' + str(i3) + '/' + str(i2) + '.ledger', 'w') as file1:
                file1.write(endend)
            file1.close()

    print(i4)