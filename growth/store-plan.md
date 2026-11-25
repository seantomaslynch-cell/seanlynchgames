# Store growth drafts (2026-11-25)

DRAFTS ONLY. Nothing here was submitted, created, uploaded or changed in App Store Connect or Google Play.
Sources: asc.py status, play.py tracks, each project's PROGRESS.md and store/ folders. Plain English, no em dashes, "team" not "club". iOS copy never names Android. Character limits are checked: event name 30, short 50, long 120.

## Store state seen today

| App | iOS (ASC) | Android (Play) |
|---|---|---|
| LifeLine | v4.3.7 build 107 live; a review submission is WAITING_FOR_REVIEW (v4.3.9 not yet live on iOS per PROGRESS) | production 4.3.9 (1795321208) |
| Hardwood GM | v2.15.0 build 61 live (READY_FOR_DISTRIBUTION) | production 2.14.2, internal 2.15.0 (not promoted) |
| Gridiron GM | v3.1.2 build 65 live | production 3.1.2 (82) |
| Gatecrash Army | v1.0.23 build 30 ACCEPTED, but review submission dcaf29f1 shows UNRESOLVED_ISSUES; v1.0.22 live | production 1.0.23 (21) |
| DiamondEdge | v1.0.3 live (US only, 1 of 175 countries); v1.0.4 in PREPARE_FOR_SUBMISSION, no build | production 1.0.3 (15) |

Open items to check before using any draft: Gatecrash iOS 1.0.23 review state, LifeLine iOS 4.3.9 timing, Hardwood Android 2.15.0 promotion.

---

## 1. Apple featuring nominations (App Store Connect > Featuring > Nominations; no API, the owner pastes it in)

Use the "App Enhancements" type for updates. Description limit is 1,000 characters. Only facts from What's New files and PROGRESS.md.

### LifeLine: 4.3.7 Careers update (nominate when 4.3.9 or later is live on iOS)
- Name: LifeLine 4.3.x, pick your career path
- Description: LifeLine is a life simulator built by one developer. You live a whole life, make the choices that shape it, and press Age to move forward. This update adds Careers, a new path through adult life with 66 careers to choose from. The game already has seasonal in-app events, including a Hanukkah event of free story cards that runs Dec 4 to Dec 12, and December and New Year events. The core game is free to play.
- Check first: confirm "66 careers" against the live What's New text (it comes from the store screenshot caption "66 CAREERS. PICK YOUR PATH!"). Drop the number if unsure.

### Hardwood GM: 2.14.0 / 2.15.0 front-office depth
- Name: Hardwood GM 2.14, two-way contracts and rivals who remember
- Description: Hardwood GM is a text-based basketball front office game built by one developer. You never play the games. You make the calls that decide them: drafts, trades, contracts, scouting and the people around the team. Update 2.14 adds real two-way contracts (one or two year deals, up to 50 active games, and a conversion before the regular season ends), a salary cap that follows the current season, and rivals who remember past deals. The whole game runs on device with no account to make. Ads are opt-in only and content packs never sell stat boosts.
- Source: store/WHATS-NEW-2.14.0.md and store/FEATURING-2.10.0.md (notes for editors). Add 2.15.0 items from its What's New text; not read here.

### Gridiron GM: 3.1.x
- Name: Gridiron GM 3.1, run a pro team from the draft room
- Description: Gridiron GM is a football management sim built by one developer. You run a pro team from the draft room to the title game, starting from a team office with a getting-started checklist. The 3.1 line adds a weekly challenge that is free and the same for everyone, plus a Holiday Challenge Weeks in-app event (Dec 20 to Jan 3). Update 3.1.2 puts the free "watch an ad for 1 token" button at the top of the Rewards sheet so it is easy to find.
- Check: confirm Full Coach Mode and other 3.1.0 items from WHATS-NEW-3.1.0.txt before adding them. Holiday event 6837159671 was submitted 2026-11-20; confirm it is approved first.

### Gatecrash Army: nominate only after 1.0.23 or 1.0.25 is clean on iOS
- Name: Gatecrash Army, grow your crowd and smash the gates
- Description: Gatecrash Army is an action runner built by one developer. Grow your army on the run, smash through every gate, and watch the math gates ahead. Chests and the daily spin are free and never sold. The app is iPhone only and free with optional purchases.
- Hold: the 1.0.23 review submission shows UNRESOLVED_ISSUES. Do not nominate until that is resolved.

### DiamondEdge: 1.0.4 (when it ships)
- Name: DiamondEdge 1.0.4, sports research in one place
- Description: DiamondEdge is a sports analytics app: matchups, player trends and game breakdowns for NFL, college football, NBA, WNBA and MLB, with a players screen that has sport filters and prop lines. The monthly plan has a 3-day free trial. Available in the United States.
- Hold: 1.0.4 has no build yet. Add the real 1.0.4 changes from its What's New once written. Do not claim any feature not in the build.

---

## 2. In-App Event drafts (draft only; asc.py event-create makes a DRAFT, but none was run)

Only content that exists. Several apps already have approved or submitted events, so the table marks overlap.

### LifeLine (existing: December in LifeLine Dec 1 to 15, Holiday Life Challenge Dec 15 to Jan 1, New Year New Life January, Hanukkah Dec 4 to 12)
1. Careers Month
   - Name (13): Careers Month
   - Short (49): Pick a career and live the whole life that follows
   - Long (101): Pick a career in LifeLine and see where it takes you. Choose your path, then press Age to move on.
   - Needs: a window that does not overlap the December events (late January or February). Confirm Careers content is in the live build first.
2. Spring Start (optional, later)
   - No new content exists yet. Skip until there is a real feature.

### Hardwood GM (existing art in store/events: awards, cup, deadline, draft, opening-night; texts in EVENT.md)
1. Two-Way Contracts Week (needs 2.14+ live, which it is on iOS)
   - Name (24): Two-Way Contracts Week
   - Short (46): Sign two-way players and watch their games
   - Long (118): Two-way deals run one or two years, up to 50 active games, and must convert before the regular season ends.
   - Art: reuse a card from store/events/draft or deadline until a real two-way screenshot is made.
2. Trade Deadline Week (already written in EVENT.md)
   - Name (19): Trade Deadline Week
   - Short (36): A hard stop. Buy, sell or stand pat.
   - Long: use the existing text in store/events/EVENT.md (it is within 120). Replace "club" with "team" in any line that uses it.

### Gridiron GM (existing: Holiday Challenge Weeks Dec 20 to Jan 3; art ready for draft, scout-the-class, playoff-push, playoffs, tag-season, title-week, trade-deadline)
1. Scout the Class
   - Name (15): Scout the Class
   - Short (45): Study the draft board and make your picks
   - Long (96): Work the draft room, scout the class and build your team. Art exists in store/events/scout-the-class.jpg.
   - Needs: copy re-checked against the live draft screens before it is created.
2. Playoff Push
   - Name (13): Playoff Push
   - Short (41): Fight for a spot in the playoffs
   - Long (89): Late in the season every game counts. Manage your team and chase a playoff berth. Art exists (playoff-push.jpg).

### Gatecrash Army (art only in store/events/holiday-2026; no copy found)
1. Gate Rush Week
   - Name (14): Gate Rush Week
   - Short (46): Smash every gate and grow your army
   - Long (110): Run, pick the right math gates and build the biggest crowd you can. Free daily spin and chests all week.
   - Hold until the 1.0.23 review issue is resolved.

### DiamondEdge (existing: Holiday Game Days Research, event 6837157410, Dec 1 to Dec 31, US only)
1. NBA Opening Weeks Research (backup if the holiday event is rejected)
   - Name (24): NBA Props Research Week
   - Short (46): AI research for NBA player props
   - Long (108): Matchups, player trends and prop lines for NBA games, each with an AI Hit Chance. Needs Pro or a free trial.
   - Source for the claim: store description and the holiday event text (113 chars, already used).

---

## 3. Product Page Optimization test ideas (existing assets only; screenshot tests need no new build)

| App | Test | Assets that exist |
|---|---|---|
| LifeLine | Control vs treatment: put the Careers screenshot ("66 CAREERS. PICK YOUR PATH!") first | store/screenshots/4.3.8-bright (10 images); change only order. Also store/ppo_v113.py is the Gatecrash-era script; use the ASC UI for LifeLine. |
| Hardwood GM | Current set vs the 10-image v2 set with team crests | store/screenshots-marketing-v2 (1242x2688). Plan is in store/ppo-plan.md. Ship only with a build that contains the crests. |
| Gridiron GM | Screenshot order: Office / team checklist first vs draft room first | store/screenshots and store/screenshots-marketing folders exist; 4 custom product pages already finished review (838666bc), so run the PPO test on the default page. |
| Gatecrash Army | Screenshot 1: gate math moment vs a crowd-size shot | store/ppo_v113.py and store/screenshots exist; creative-assets has header and search art. Icon test only if an alternate icon is drawn (none found). |
| DiamondEdge | Screenshot 1: prop lines with Hit Chance vs the players screen | store/creative-assets (live logo-512 and live App Store shots). US-only listing, so traffic is small: run longer. |

Rule: one change per test, 50/50 split, run until Apple shows confidence. Never test an icon without an approved alternate.

---

## 4. Google Play store listing experiments (Play Console > Store listing experiments; set up by the owner)

| App | Experiment | Variant idea |
|---|---|---|
| LifeLine | Short description (80 chars max) | A: current. B: "Live a whole life. Pick a career, make the choices, press Age." Check length before pasting (63). |
| Hardwood GM | Feature graphic | A: current. B: a graphic using a real screen with the Draft or Trade Deadline view; art in store/events and store/screenshots-marketing-v2. |
| Gridiron GM | Short description | A: current. B: "Run a pro football team from the draft room to the title game." (66). |
| Gatecrash Army | Short description | A: current. B: "Grow your army on the run. Smash every gate. Math gates ahead." (62). |
| DiamondEdge | Screenshot order | B: lead with the prop lines screen with sport filters. Android listing is US-focused; keep the test 14+ days. |

Play listing text must not name iOS, App Store or iPhone-only claims. Play experiments cover the default listing only; keep each test to one change.

---

## Not done
- Nothing submitted or created. No store reads beyond status, tracks and local files.
- Not read: Hardwood 2.15.0 What's New, Gridiron 3.1.0 and 3.1.1 What's New in full, DiamondEdge 1.0.4 notes, Gatecrash 1.0.23 notes. Verify the claims above against them before use.
