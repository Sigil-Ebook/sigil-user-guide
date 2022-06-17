# <center>Sigil 사용자 가이드를 한국어로 번역하기 위한 저장소입니다.</center>
<br/>

## <center>(원문)번역을 위한 지침</center>

<br/>

1. 예술적/미학적 변화를 주지 마십시오! 우리는 콘텐츠 업데이트 및 수정, 또는 새로운 메뉴나 새로운 기능을 보여주는 업데이트된 스크린샷에만 관심이 있습니다. 개인 스타일이나 서식 기본 설정을 반영하기 위해 epub 스타일을 수정할 수 없습니다. 스타일 변경이나 "업그레이드"가 포함된 풀 리퀘스트는 거절될 것입니다(물론 그러한 작업이 사전 승인되지 않은 경우).


2. __적은 것이 가장 좋습니다.__ 큰 범위의 전면적인 변경 보다는 국소적이지만 디테일 한 번경이 우선적으로 반영됩니다. 변경 사항을 반영할 때 가이드 전체를 다시 검토하는 것은 시간이 많이 걸리고 어렵습니다. 기본 틀은 그대로 두고 새로운 변경사항이나 부분적인 오류를 중심으로 수정해 주십시요.(이 부분은 영문 내용을 의역하였습니다)

3. __아무것도 부수지 마십시오.__ epub을 손상시키거나 유효성 검사 문제를 일으키는 변경 사항은 거부됩니다. 내용을 수정할 때 epub 구조가 손상되지 않고 사양을 준수하는지 확인을 한 후 반영을 요청하십시요.

<br/>
<br/>

## <center>한국어 번역을 위한 지침</center>

<br/>

__가장 중요한 원칙__ 한국어 번역 이외의 모든 지침은 Sigil User Guide의 기본 원칙(https://github.com/Sigil-Ebook/sigil-user-guide)을 따라야 합니다.

1. __원문은 그대로 두세요__ 내용의 검수를 위해 원문 밑에 한국어 번역문을 추가합니다.

__예시__
  &lt;p&gt;The EPUB (electronic publication) format is one of the most popular file formats for ebooks. It is an open and freely available standard that can be used by anyone.&lt;/p&gt;

  <p>EPUB(전자 출판) 형식은 가장 널리 사용되는 전자책 파일 형식 중 하나입니다. 누구나 사용할 수 있는 개방적이고 자유롭게 사용할 수 있는 표준입니다.</p>

2. __의역을 해도 됩니다__ 내용을 더 쉽게 설명할 수 있다면 의역을 해도 됩니다. 

3. __Github 사용법을 모르면 HTML로 다운 받아 번역을 하세요__ Github 사용법을 모르면 텍스트만 복사해 PC에서 작업을 하세요. 번역 한 파일을 Issue 게시판에 올리면 확인 후 반영하겠습니다.
<br/>
<br/>

## <center>선호하는 워크플로</center>

<br/>

- 이 리포지토리를 자신의 Github 계정에 포크하고 로컬 복사본을 컴퓨터에 복제합니다.

- [FolderIn Sigil 플러그인](https://www.mobileread.com/forums/showthread.php?t=293649)을 사용하여 복제된 로컬 저장소의 "src" 디렉토리 내용을 Sigil로 로드합니다.

- 편집을 수행합니다(필요한 경우 로컬 임시 epub에 변경 사항 저장). 완료한 후 "Mend and Prettify"를 사용하고 항상 epub이 오류 없이 유효성을 검사하는지 확인하십시오. 그런 다음 준비가 되면 [FolderOut Sigil 플러그인](https://www.mobileread.com/forums/showthread.php?t=293649)을 사용하여 복제된 로컬 저장소의 "src" 디렉토리에 내용을 다시 저장합니다.

- 일반 git 도구를 사용하여 차이점을 확인한 다음 만족하면 변경 사항을 커밋하고 Github 포크에 푸시합니다.

- 변경 사항을 검토하고 프로젝트에 가져올 수 있도록 Github 계정에서 새 Pull Request를 만드세요.

<br/>

----

<br/>

문제가 발생하면 [Mobileread의 Sigil 지원 포럼](https://www.mobileread.com/forums/forumdisplay.php?f=203)에서 언제든지 도움을 요청하십시오.
