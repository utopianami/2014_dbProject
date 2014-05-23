/*글 포스팅  1.글적기, 2.qooq하기, 3.tag달기 */
select id from article where url = ?; /*url확인*/
insert into article (title, url, contents ) values (?, ?, ?); /*없다면 insert*/
insert into qooq (user_uid, article_aid) values (?, ?);  /*qooq insert*/
insert into article_has_tag (aid, tid) values (?, ?); /*tag연결 */

/*단어 넣기  단어 존재 확인 -> 단어 넣기*/
select id from word where word = ?;
insert into article_has_word (aid, wid) values (?, ?);


/*전체글 가지고 오기  각 글의 tag리스트, 전체 글 */
select  t2.name from `article_has_tag` t1 + left outer join tag t2 on t1.tid = t2.`tid` where t1.aid = ?;
select aid, title, from article;

/*개인 글 가져오기 개인글정보 +qooq정보*/
SELECT aid, title, url, contents, readCount, titleImg FROM article WHERE aid = ?;
SELECT T2.uid, T2.name, T2.profileImg FROM qooq T1 LEFT OUTER JOIN user T2 ON T2.uid = T1.user_uid WHERE T1.article_aid = ?;