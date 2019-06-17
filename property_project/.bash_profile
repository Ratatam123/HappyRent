## key for Flask App
export SECRET_KEY='3516faa3660d50c1f5b34496db9e4819'

## Google OAuth keys
export GOOGLE_OAUTH_CLIENT_ID='646163642970-koimt79vmr3355q1sldsd9e68hvvr336.apps.googleusercontent.com'
export GOOGLE_OAUTH_CLIENT_SECRET='asUsmHtCv1TsfWa-gsJBJoOd'

# Setting PATH for Python 3.6
# The original version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.6/bin:${PATH}"
export PATH

# added by Anaconda3 5.1.0 installer
export PATH="/Users/lorenz_123/anaconda3/bin:$PATH"

[[ -s "$HOME/.rvm/scripts/rvm" ]] && source "$HOME/.rvm/scripts/rvm" # Load RVM into a shell session *as a function*

# The next line updates PATH for the Google Cloud SDK.
if [ -f '/Users/lorenz_123/Desktop/Udacity-Fullstack/google-cloud-sdk/path.bash.inc' ]; then . '/Users/lorenz_123/Desktop/Udacity-Fullstack/google-cloud-sdk/path.bash.inc'; fi

# The next line enables shell command completion for gcloud.
if [ -f '/Users/lorenz_123/Desktop/Udacity-Fullstack/google-cloud-sdk/completion.bash.inc' ]; then . '/Users/lorenz_123/Desktop/Udacity-Fullstack/google-cloud-sdk/completion.bash.inc'; fi

### Udacity git-setup
# Enable tab completion
source ~/.udacity-terminal-config/git-completion.bash

# Change command prompt
source ~/.udacity-terminal-config/git-prompt.sh

# colors!
red="\[\033[38;5;203m\]"
green="\[\033[38;05;38m\]"
blue="\[\033[0;34m\]"
reset="\[\033[0m\]"

export GIT_PS1_SHOWDIRTYSTATE=1

# '\u' adds the name of the current user to the prompt
# '\$(__git_ps1)' adds git-related stuff
# '\W' adds the name of the current directory
export PS1="$red\u$green\$(__git_ps1)$blue \W
$ $reset"