import matplotlib.pyplot as plt

plt.plot( [1,2], [1,2], 'o' )
plt.xlim( [0,3] )
plt.ylim( [0,3] )

plt.annotate( "", xy=(1,1), xytext=(1.3, 2.5),
              arrowprops=dict( arrowstyle="->" ) )
plt.annotate( '', xy=(2,2), xytext=(1.3, 2.5),
              arrowprops=dict( arrowstyle="->" ) )
plt.annotate( 'Some annotation', xy=(1.3, 2.5),
              xytext=(1.3, 2.5) , va = "bottom", ha="center" )

plt.annotate( "", xy=(1,1), xytext=(1.5, .5),
              arrowprops=dict( arrowstyle="->",shrinkA=0 ) )
plt.annotate( '', xy=(2,2), xytext=(1.5, .5),
              arrowprops=dict( arrowstyle="->",shrinkA=0 ) )
plt.annotate( 'Yet another annotation', xy=(1.5, .5),
              xytext=(1.5, .5) , va = "top", ha="left" )

plt.show()