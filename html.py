

def hh():
    hh = '''<html>
        <head>
            <link rel="stylesheet" href="templates/styles.css">
        </head>
        <body>
        <div id="fullpage">'''
    return hh
def hb():
    hb = '''
    </div>
    </body>
    </html>
    '''
    return hb

def html(num, author, time, comment, score):
    html = f'''
    <div id="id_{num}">
    <div class="CommentTree__comment m-comment m-toplevel" style="padding-left: 16px;">
       <div>
          <div class="Comment in-comment-tree m-top">
             <div class="Comment__header" id="htmc0mq">
                <div class="CommentHeader ">
                   <table class="CommentHeader__table">
                      <tbody>
                         <tr>
                            <td class="CommentHeader__col2">
                               <span class="CommentHeader__container">
                                  <a href="/user/indylerone93/" class="CommentHeader__username "><img alt="u/indylerone93 avatar" class="CommentHeader__avatar " src="templates/redditor.png"></a>
                                  <div class="CommentHeader__timestamp"></a><span>{author}</span>{time}</div>
                               </span>
                            </td>
                            <td class="CommentHeader__colMore">

                            </td>
                         </tr>
                      </tbody>
                   </table>
                </div>
             </div>
             <div>
                <a href="/r/MurderedByWords/comments/s9f0bj/comment/htmc0mq/" rel="nofollow" class="sr-only"></a>
                <div class="Comment__body ">
                   <div class="md">
                      {comment}
                   </div>
                </div>
             </div>
             <span>
                <script type="text/javascript">__recordMark('first-comment-visible');__clearMarks('first-comment-visible');__perfMark('first-comment-visible');</script><script>__recordMark('first-comment-visible');__clearMarks('first-comment-visible');__perfMark('first-comment-visible');</script>
             </span>
             <div class="Comment__toolsContainer clearfix ">
                <div class="Comment__tools">
                   <div>
                      <div class="DropdownModalWrapper"></div>
                      <div class="VotingBox _3H4qDQeWDrSuPhQT4VfGyR m-action-bar-redesign">
                         <div class="VotingBox__upvote icon icon-upvote m-redesign m-action-bar-redesign ">
                            <svg class="VotingBox__svg" height="16" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg">
                               <path clip-rule="evenodd" d="m8 .200001c.17143 0 .33468.073332.44854.201491l7.19996 8.103998c.157.17662.1956.42887.0988.64437-.0968.21551-.3111.35414-.5473.35414h-3.4v5.496c0 .3314-.2686.6-.6.6h-6.4c-.33137 0-.6-.2686-.6-.6v-5.496h-3.4c-.236249 0-.450507-.13863-.547314-.35414-.096807-.2155-.058141-.46775.09877-.64437l7.200004-8.103998c.11386-.128159.27711-.201491.44854-.201491zm-5.86433 8.103999h2.66433c.33137 0 .6.26863.6.6v5.496h5.2v-5.496c0-.33137.2686-.6.6-.6h2.6643l-5.8643-6.60063" fill-rule="evenodd"></path>
                            </svg>
                         </div>
                         <div class="VotingBox__score m-redesign m-action-bar-redesign _3SmWG9I6J6ldV9Zeon-EwN ">{score}</div>
                         <div class="VotingBox__downvote icon icon-downvote m-redesign m-action-bar-redesign ">
                            <svg class="VotingBox__svg" height="16" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg">
                               <path clip-rule="evenodd" d="M4.2 0.799997C4.2 0.468626 4.46863 0.199997 4.8 0.199997H11.2C11.5314 0.199997 11.8 0.468626 11.8 0.799997V6.304H15.2C15.4363 6.304 15.6506 6.44269 15.7474 6.65827C15.8441 6.87385 15.8054 7.12615 15.6483 7.30273L8.44835 15.3987C8.33449 15.5268 8.17133 15.6 8 15.6C7.82867 15.6 7.66551 15.5268 7.55165 15.3987L0.351652 7.30273C0.194618 7.12615 0.15585 6.87385 0.252626 6.65827C0.349402 6.44269 0.563698 6.304 0.8 6.304H4.2V0.799997ZM5.4 1.4V6.904C5.4 7.23537 5.13137 7.504 4.8 7.504H2.13654L8 14.0971L13.8635 7.504H11.2C10.8686 7.504 10.6 7.23537 10.6 6.904V1.4H5.4Z" fill-rule="evenodd"></path>
                            </svg>
                         </div>
                      </div>
                      <span class="_1UC3OWGfqCsYvxcSoPUm3w icon icon-reply2">
                         <svg class="_3Kx-yL7qiO1F6uot_gPDCQ" height="15" viewBox="0 0 16 15" width="16" xmlns="http://www.w3.org/2000/svg">
                            <path clip-rule="evenodd" d="M4 0C2.99218 0 2.02563 0.400356 1.31299 1.11299C0.600356 1.82563 0.2 2.79218 0.2 3.8V8.6C0.2 9.60782 0.600356 10.5744 1.31299 11.287C2.02563 11.9996 2.99218 12.4 4 12.4H5.35147L7.57528 14.6238C7.57543 14.624 7.57559 14.6241 7.57574 14.6243C7.81005 14.8586 8.18995 14.8586 8.42426 14.6243L10.6485 12.4H12C13.0078 12.4 13.9744 11.9996 14.687 11.287C15.3996 10.5744 15.8 9.60782 15.8 8.6V3.8C15.8 2.79218 15.3996 1.82563 14.687 1.11299C13.9744 0.400356 13.0078 0 12 0H4ZM8 13.3515L9.97574 11.3757C10.0883 11.2632 10.2409 11.2 10.4 11.2H12C12.6896 11.2 13.3509 10.9261 13.8385 10.4385C14.3261 9.95088 14.6 9.28956 14.6 8.6V3.8C14.6 3.11044 14.3261 2.44912 13.8385 1.96152C13.3509 1.47393 12.6896 1.2 12 1.2H4C3.31044 1.2 2.64912 1.47393 2.16152 1.96152C1.67393 2.44912 1.4 3.11044 1.4 3.8V8.6C1.4 9.28956 1.67393 9.95088 2.16152 10.4385C2.64912 10.9261 3.31044 11.2 4 11.2H5.6C5.76568 11.2 5.91568 11.2672 6.02426 11.3757C6.02434 11.3758 6.02442 11.3759 6.0245 11.376L8 13.3515Z" fill-rule="evenodd"></path>
                         </svg>
                         <span class="_2RaAHWm0eiqPhxjaiJZvWF">Reply</span>
                      </span>
                      <button class="_2OSerrGqsksmXpb-ulVmEG" aria-label="Give award">
                         <svg height="16" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg">
                            <path d="M8.00001 4.20001C8.33138 4.20001 8.60001 4.46864 8.60001 4.80001V7.40001H11.2C11.5314 7.40001 11.8 7.66863 11.8 8.00001C11.8 8.33138 11.5314 8.60001 11.2 8.60001H8.60001V11.2C8.60001 11.5314 8.33138 11.8 8.00001 11.8C7.66864 11.8 7.40001 11.5314 7.40001 11.2V8.60001H4.80001C4.46864 8.60001 4.20001 8.33138 4.20001 8.00001C4.20001 7.66863 4.46864 7.40001 4.80001 7.40001H7.40001V4.80001C7.40001 4.46864 7.66864 4.20001 8.00001 4.20001Z" fill="inherit"></path>
                            <path clip-rule="evenodd" d="M8.00001 0.197662C7.51154 0.197662 7.03701 0.360229 6.65119 0.659651L1.12676 4.82489L1.12009 4.83007C0.735744 5.12843 0.451895 5.53724 0.306658 6.00162C0.161479 6.46581 0.161927 6.96385 0.307603 7.42788L2.41007 14.167C2.54958 14.634 2.83463 15.0444 3.22372 15.3381C3.61402 15.6328 4.08847 15.7947 4.57749 15.8L11.408 15.8001L11.4145 15.8C11.9036 15.7947 12.378 15.6328 12.7683 15.3381C13.1573 15.0444 13.4423 14.6342 13.5819 14.1673L15.6924 7.42781C15.8383 6.96365 15.8386 6.46598 15.6934 6.00162C15.5481 5.53724 15.2643 5.12838 14.88 4.83002L9.34885 0.659662C8.96303 0.360232 8.48849 0.197662 8.00001 0.197662ZM7.38501 1.60914C7.56072 1.47209 7.77718 1.39766 8.00001 1.39766C8.22285 1.39766 8.43925 1.47215 8.61496 1.6092L14.1471 5.7803C14.3364 5.92828 14.4763 6.1304 14.5481 6.35982C14.6202 6.59045 14.6199 6.83817 14.5474 7.06871L12.4354 13.8127L12.4328 13.8214C12.3667 14.0444 12.2308 14.2403 12.0452 14.3804C11.8604 14.52 11.6359 14.5969 11.4044 14.6H4.58765C4.35613 14.5969 4.13161 14.52 3.94678 14.3804C3.76118 14.2403 3.62542 14.0444 3.55931 13.8214L1.45278 7.06932L1.45242 7.06816C1.37998 6.83763 1.37982 6.59045 1.45195 6.35982C1.5237 6.13039 1.66358 5.92827 1.85295 5.7803L7.37728 1.61517L7.38501 1.60914Z" fill="inherit" fill-rule="evenodd"></path>
                         </svg>
                      </button>
                   </div>
                   <div class="AwardsBar"></div>
                </div>
             </div>
          </div>
       </div>
    </div>
    </div>
    '''
    return html

def header(num, title, author, time, comment, score):
    header = f'''
    <div id="id_{num}">
    <article class="Post size-default m-redesign" id="t3_s9yru8"><div class="Post__header-wrapper"><header class="PostHeader m-default m-redesign m-single"><div class="PostHeader__metadata-container"><div class="PostHeader__post-descriptor-line"><div class="PostHeader__post-descriptor-line-overflow"><span><span class="PostHeader__post-meta-container"><a href="/user/_Role_007/" class="PostHeader__author-link m-pur-header"><img alt="u/_Role_007 avatar" class="PostHeader__avatar " src="https://www.redditstatic.com/mweb2x/img/snoovatars/snoovatar_11.png" style="background-color:#0DD3BB">{author}</a><span class="PostHeader__separator PostHeader__flush-w-icon"></span>{time}</span><span class="PostHeader__separator PostHeader__flush-w-icon"></span><span><span class="PostHeader__nsfw-text"><span class="icon icon-nsfw nsfw"></span><span class="PostHeader__flush-w-icon">NSFW</span></span></span></span></div></div><div class="PostHeader__metadata "></div><form class="PostHeader__join-form-experiment" action="/actions/toggle-subreddit-subscription" method="post"><input type="hidden" name="subredditName" value="jokes"><input type="hidden" name="fullName" value="t5_2qh72"><input type="hidden" name="isSubscriber" value="false"><button class="JoinButtonFull m-subscribe" type="submit">Join</button></form><div class="PostHeader__overflowMenu icon icon-seashells"></div></div><h1 class="PostHeader__post-title-line ">{title}</h1><div class="PostHeader__post-descriptor-line"><div class="PostHeader__post-descriptor-line-overflow m-small"><span class="PostHeader__link-flair m-pill">Long</span></div></div><span><script type="text/javascript">__recordMark('meaningful-paint');__clearMarks('meaningful-paint');__perfMark('meaningful-paint');</script><script>__recordMark('meaningful-paint');__clearMarks('meaningful-paint');__perfMark('meaningful-paint');</script></span></header></div><div class="PostContent size-default"><div><div class="PostContent__selftextContainer "><div class="PostContent__selftext "><!-- SC_OFF --><div class="md">
    {comment}
</div><!-- SC_ON --></div><span><script type="text/javascript">__recordMark('meaningful-paint');__clearMarks('meaningful-paint');__perfMark('meaningful-paint');</script><script>__recordMark('meaningful-paint');__clearMarks('meaningful-paint');__perfMark('meaningful-paint');</script></span></div></div></div><footer class="PostFooter m-redesign m-single"><div class="PostFooter__vote-and-tools-wrapper">
<div class="VotingBox PostFooter__votingBox "><div class="VotingBox__upvote icon icon-upvote m-redesign m-large "><svg class="VotingBox__svg" height="16" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="m8 .200001c.17143 0 .33468.073332.44854.201491l7.19996 8.103998c.157.17662.1956.42887.0988.64437-.0968.21551-.3111.35414-.5473.35414h-3.4v5.496c0 .3314-.2686.6-.6.6h-6.4c-.33137 0-.6-.2686-.6-.6v-5.496h-3.4c-.236249 0-.450507-.13863-.547314-.35414-.096807-.2155-.058141-.46775.09877-.64437l7.200004-8.103998c.11386-.128159.27711-.201491.44854-.201491zm-5.86433 8.103999h2.66433c.33137 0 .6.26863.6.6v5.496h5.2v-5.496c0-.33137.2686-.6.6-.6h2.6643l-5.8643-6.60063" fill-rule="evenodd"></path></svg></div>
<div class="VotingBox__score m-redesign m-large ">{score}</div><div class="VotingBox__downvote icon icon-downvote m-redesign m-large "><svg class="VotingBox__svg" height="16" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M4.2 0.799997C4.2 0.468626 4.46863 0.199997 4.8 0.199997H11.2C11.5314 0.199997 11.8 0.468626 11.8 0.799997V6.304H15.2C15.4363 6.304 15.6506 6.44269 15.7474 6.65827C15.8441 6.87385 15.8054 7.12615 15.6483 7.30273L8.44835 15.3987C8.33449 15.5268 8.17133 15.6 8 15.6C7.82867 15.6 7.66551 15.5268 7.55165 15.3987L0.351652 7.30273C0.194618 7.12615 0.15585 6.87385 0.252626 6.65827C0.349402 6.44269 0.563698 6.304 0.8 6.304H4.2V0.799997ZM5.4 1.4V6.904C5.4 7.23537 5.13137 7.504 4.8 7.504H2.13654L8 14.0971L13.8635 7.504H11.2C10.8686 7.504 10.6 7.23537 10.6 6.904V1.4H5.4Z" fill-rule="evenodd"></path></svg></div></div>

<a href="/r/Jokes/comments/s9yru8/so_a_village_boy_and_a_modern_girl_fall_in_love/" class="PostFooter__hit-area PostFooter__comments-link" rel="nofollow"><svg class="PostFooter__comments-icon-new" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M4.00001 0C2.99219 0 2.02564 0.400356 1.31301 1.11299C0.600368 1.82563 0.200012 2.79218 0.200012 3.8V8.6C0.200012 9.60782 0.600368 10.5744 1.31301 11.287C2.02564 11.9996 2.99219 12.4 4.00001 12.4H5.35149L7.5753 14.6238C7.57545 14.624 7.5756 14.6241 7.57575 14.6243C7.81006 14.8586 8.18996 14.8586 8.42428 14.6243L10.6485 12.4H12C13.0078 12.4 13.9744 11.9996 14.687 11.287C15.3997 10.5744 15.8 9.60782 15.8 8.6V3.8C15.8 2.79218 15.3997 1.82563 14.687 1.11299C13.9744 0.400356 13.0078 0 12 0H4.00001ZM8.00001 13.3515L9.97575 11.3757C10.0883 11.2632 10.2409 11.2 10.4 11.2H12C12.6896 11.2 13.3509 10.9261 13.8385 10.4385C14.3261 9.95088 14.6 9.28956 14.6 8.6V3.8C14.6 3.11044 14.3261 2.44912 13.8385 1.96152C13.3509 1.47393 12.6896 1.2 12 1.2H4.00001C3.31045 1.2 2.64913 1.47393 2.16153 1.96152C1.67394 2.44912 1.40001 3.11044 1.40001 3.8V8.6C1.40001 9.28956 1.67394 9.95088 2.16153 10.4385C2.64913 10.9261 3.31045 11.2 4.00001 11.2H5.60001C5.7657 11.2 5.91569 11.2672 6.02427 11.3757C6.02435 11.3758 6.02443 11.3759 6.02452 11.376L8.00001 13.3515Z" fill="inherit" fill-rule="evenodd"></path></svg>195</a><span class="PostFooter__vertical-divider"></span><span class="Intercourse smaller-margin PostFooter__share "><svg class="Intercourse__icon v1" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg"><path d="M8.47298 1.17643C8.36435 1.06744 8.21406 1 8.04802 1C7.88694 1 7.74068 1.06348 7.6329 1.16679L7.62376 1.17574L4.42376 4.37574C4.18944 4.61005 4.18944 4.98995 4.42376 5.22426C4.65807 5.45858 5.03797 5.45858 5.27229 5.22426L7.44802 3.04853V10.4C7.44802 10.7314 7.71665 11 8.04802 11C8.3794 11 8.64802 10.7314 8.64802 10.4V3.04853L10.8238 5.22426C11.0581 5.45858 11.438 5.45858 11.6723 5.22426C11.9066 4.98995 11.9066 4.61005 11.6723 4.37574L8.47298 1.17643Z" fill="inherit"></path><path d="M3.04802 8C3.04802 7.66863 2.77939 7.4 2.44802 7.4C2.11665 7.4 1.84802 7.66863 1.84802 8V12.8C1.84802 13.3835 2.07981 13.9431 2.49239 14.3556C2.90497 14.7682 3.46455 15 4.04802 15H12.048C12.6315 15 13.1911 14.7682 13.6037 14.3556C14.0162 13.9431 14.248 13.3835 14.248 12.8V8C14.248 7.66863 13.9794 7.4 13.648 7.4C13.3167 7.4 13.048 7.66863 13.048 8V12.8C13.048 13.0652 12.9427 13.3196 12.7551 13.5071C12.5676 13.6946 12.3132 13.8 12.048 13.8H4.04802C3.78281 13.8 3.52845 13.6946 3.34092 13.5071C3.15338 13.3196 3.04802 13.0652 3.04802 12.8V8Z" fill="inherit"></path></svg><span class="Intercourse__text">Share</span></span></div><div class="DropdownModalWrapper"></div></footer></article>
     </div>
    '''
    return header