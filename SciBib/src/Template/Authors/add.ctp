<!--
   Copyright {2017} {University Konstanz -  Data Analysis and Visualization Group}

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
-->
<nav class="large-3 medium-4 columns" id="actions-sidebar">
    <ul class="side-nav">
        <li class="heading"><?= __('Actions') ?></li>
        <li><?= $this->Html->link($this->Html->image('/img/author.png', ['width' => '16', 'height' => '16']) . ' ' . __('List authors'), ['controller' => 'Authors', 'action' => 'index'], ['escape' => false]) ?></li>
    </ul>
</nav>
<div class="authors form large-9 medium-8 columns content">
    <?= $this->Form->create($author) ?>
    <fieldset>
        <legend><?= __('Add Author') ?></legend>
        <?php
        echo $this->Form->input('forename');
        echo $this->Form->input('surname');
        echo $this->Form->input('website');
        ?>
        <p style="font-size: 0.9rem"> &nbsp&nbsp&nbsp&nbsp e.g. http://vis.uni-konstanz.de/mitglieder/keim/ </p>
    </fieldset>
    <?= $this->Form->button(__('Submit')) ?>
    <?= $this->Form->end() ?>
</div>