from distutils.core import setup

setup(name='django-annotatetext',
      version='0.1beta',
      description='AnnotateText is a Django App that lets you select parts of a text of some model and write an annotation for it.',
      long_description=open('README.mkd').read(),
      author='Stefan Wehrmeyer',
      author_email='mail@stefanwehrmeyer.com',
      url='https://github.com/hasadna/django-annotatetext',
      packages=['annotatetext'],
      package_data={'annotatetext':['media/annotatetext/*', 'templates/annotatetext/*']},
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )
